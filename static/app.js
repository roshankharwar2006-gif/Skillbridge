// Small helper object. Progress is saved in the browser with localStorage.
const SB = {
  get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} },
  doneCount(id) { return this.get("lessons-" + id, []).length; },

  // ----- Courses -----
  renderBars() {
    document.querySelectorAll("[data-course]").forEach(el => {
      el.style.width = (this.doneCount(el.dataset.course) / el.dataset.total * 100) + "%";
    });
  },
  courseInit(id, total) {
    const boxes = document.querySelectorAll("[data-lesson]");
    let done = this.get("lessons-" + id, []);
    const paint = () => {
      document.getElementById("course-bar").style.width = (done.length / total * 100) + "%";
      document.getElementById("course-text").textContent = done.length + " of " + total + " lessons done";
    };
    boxes.forEach(b => {
      b.checked = done.includes(+b.dataset.lesson);
      b.addEventListener("change", () => {
        done = done.filter(n => n !== +b.dataset.lesson);
        if (b.checked) done.push(+b.dataset.lesson);
        this.set("lessons-" + id, done); paint();
      });
    });
    paint();
  },
  renderOverall(ids, totals) {
    let d = 0, t = 0;
    ids.forEach((id, i) => { d += this.doneCount(id); t += totals[i]; });
    const pct = t ? Math.round(d / t * 100) : 0;
    document.getElementById("overall-bar").style.width = pct + "%";
    document.getElementById("overall-pct").textContent = pct + "%";
    const mark = (n, ok) => document.querySelector('[data-done="' + n + '"]').classList.toggle("ok", ok);
    mark("lessons", pct === 100); mark("resume", !!this.get("resume-built", false));
    mark("interview", this.get("practised-total", 0) >= 5);
  },

  // ----- Resume builder -----
  resumeInit() {
    const form = document.getElementById("rform"), out = document.getElementById("preview");
    const saved = this.get("resume", {});
    const esc = s => s.replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
    const lines = s => s.split("\n").map(x => x.trim()).filter(Boolean);
    const list = a => a.length ? "<ul>" + a.map(x => "<li>" + esc(x) + "</li>").join("") + "</ul>" : '<p class="empty">Not added yet</p>';
    const draw = () => {
      const v = Object.fromEntries(new FormData(form));
      this.set("resume", v); if (v.name) this.set("resume-built", true);
      const contact = [v.phone, v.email, v.city].filter(Boolean).map(esc).join(" | ");
      out.innerHTML = "<h1>" + esc(v.name || "Your Name") + "</h1>" +
        (v.role ? '<p class="role">' + esc(v.role) + "</p>" : "") +
        '<p class="contact">' + (contact || "Phone | Email | City") + "</p>" +
        (v.summary ? "<h2>About me</h2><p>" + esc(v.summary) + "</p>" : "") +
        "<h2>Education</h2>" + list(lines(v.education || "")) +
        "<h2>Skills</h2>" + list((v.skills || "").split(",").map(x => x.trim()).filter(Boolean)) +
        "<h2>Projects / Experience</h2>" + list(lines(v.experience || ""));
    };
    Object.entries(saved).forEach(([k, val]) => { if (form.elements[k]) form.elements[k].value = val; });
    form.addEventListener("input", draw); draw();
  },
  clearResume() { if (confirm("Clear all resume details?")) { this.set("resume", {}); location.reload(); } },

  // ----- Mock interview -----
  interviewInit(data) {
    let cat = Object.keys(data)[0], order = [], i = 0, timer = null, left = 60, today = 0;
    const $ = id => document.getElementById(id);
    const shuffle = a => a.map(x => [Math.random(), x]).sort((p, q) => p[0] - q[0]).map(p => p[1]);
    const stop = () => { clearInterval(timer); timer = null; $("tbtn").textContent = "Start timer"; };
    const show = () => {
      stop(); left = 60; $("time").textContent = left; $("time").classList.remove("low");
      $("tip").hidden = true; $("showtip").textContent = "Show tip";
      const q = data[cat][order[i]];
      $("question").textContent = q.q; $("tip").textContent = q.tip;
      $("qcount").textContent = "Question " + (i + 1) + " of " + order.length;
    };
    const pick = c => { cat = c; order = shuffle([...data[c].keys()]); i = 0; show(); };
    document.querySelectorAll(".chip").forEach(b => b.addEventListener("click", () => {
      document.querySelectorAll(".chip").forEach(x => x.classList.remove("on")); b.classList.add("on"); pick(b.dataset.cat);
    }));
    $("showtip").addEventListener("click", () => { $("tip").hidden = !$("tip").hidden; $("showtip").textContent = $("tip").hidden ? "Show tip" : "Hide tip"; });
    $("next").addEventListener("click", () => {
      today++; $("practised").textContent = today; this.set("practised-total", this.get("practised-total", 0) + 1);
      i = (i + 1) % order.length; show();
    });
    $("tbtn").addEventListener("click", () => {
      if (timer) return stop();
      $("tbtn").textContent = "Stop";
      timer = setInterval(() => {
        left--; $("time").textContent = left; $("time").classList.toggle("low", left <= 10);
        if (left <= 0) stop();
      }, 1000);
    });
    pick(cat);
  }
};
