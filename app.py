import json, os, sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from data import COURSES, INTERVIEW, TIPS

app = Flask(__name__)
app.secret_key = "change-this-secret"          # needed for flash messages
DB = os.path.join(os.path.dirname(__file__), "bootcamp.db")
ADMIN_KEY = "bootcamp123"                       # simple demo password for /admin


def db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("""CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, phone TEXT,
        email TEXT, education TEXT, course TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP)""")
    return con


@app.route("/")
def home():
    return render_template("index.html", courses=COURSES, tips=TIPS)


@app.route("/courses")
def courses():
    return render_template("courses.html", courses=COURSES)


@app.route("/courses/<cid>")
def course(cid):
    c = next((c for c in COURSES if c["id"] == cid), None)
    if not c:
        abort(404)
    return render_template("course.html", c=c)


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/interview")
def interview():
    return render_template("interview.html", data=json.dumps(INTERVIEW), cats=list(INTERVIEW))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        f = request.form
        name, phone = f.get("name", "").strip(), f.get("phone", "").strip()
        if not name or not phone.isdigit() or len(phone) != 10:
            flash("Please enter your name and a 10-digit phone number.", "error")
            return render_template("register.html", courses=COURSES, f=f)
        with db() as con:
            con.execute("INSERT INTO students(name,age,phone,email,education,course) VALUES(?,?,?,?,?,?)",
                        (name, f.get("age") or None, phone, f.get("email"), f.get("education"), f.get("course")))
        flash(f"Thank you, {name}! You are registered. We will call you soon.", "ok")
        return redirect(url_for("register"))
    return render_template("register.html", courses=COURSES, f={})


@app.route("/admin")
def admin():
    if request.args.get("key") != ADMIN_KEY:
        abort(403)
    rows = db().execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    return render_template("admin.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
