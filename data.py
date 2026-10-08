# All course and interview content lives here, so it is easy to edit.

COURSES = [
    {"id": "computer-basics", "title": "Computer Basics", "level": "Beginner", "hours": 3,
     "summary": "Learn to use a computer confidently: files, folders, typing and safety.",
     "link": ("GCFGlobal: Computer Basics", "https://edu.gcfglobal.org/en/computerbasics/"),
     "lessons": [
        {"t": "Parts of a computer", "body": "A computer has input devices (keyboard, mouse), a processor (the brain), memory (RAM), storage (hard disk/SSD) and output devices (screen, printer).", "tip": "Practice: name 5 parts of the computer in front of you."},
        {"t": "Files and folders", "body": "A file holds your work. A folder keeps files organised. Use clear names like Resume_Rohit_2026.docx instead of New1.docx.", "tip": "Create a folder called 'Job Documents' and keep your resume and certificates in it."},
        {"t": "Typing and shortcuts", "body": "Ctrl+C copy, Ctrl+V paste, Ctrl+Z undo, Ctrl+S save. Touch typing at 30 words per minute is enough for most entry-level jobs.", "tip": "Practice 10 minutes a day on a free typing site."},
        {"t": "Staying safe", "body": "Use strong passwords, never share your OTP, and do not click unknown links. Keep your system updated.", "tip": "A good password has 12+ characters with letters, numbers and symbols."}]},
    {"id": "office-tools", "title": "Office Tools (Word, Excel, Sheets)", "level": "Beginner", "hours": 5,
     "summary": "Create letters, tables and simple calculations used in almost every office job.",
     "link": ("GCFGlobal: Excel", "https://edu.gcfglobal.org/en/excel/"),
     "lessons": [
        {"t": "Writing in Word / Docs", "body": "Use headings, bold, bullet points and alignment to make documents neat. Always run spell-check before sending.", "tip": "Write a one-page leave application in Word."},
        {"t": "Spreadsheet basics", "body": "A spreadsheet has rows, columns and cells. Type =SUM(A1:A5) to add numbers and =AVERAGE(A1:A5) for the average.", "tip": "Make a monthly expense sheet with a total at the bottom."},
        {"t": "Charts and sorting", "body": "Select your data and insert a chart to show it visually. Use Sort and Filter to find information quickly.", "tip": "Turn your expense sheet into a pie chart."}]},
    {"id": "internet-email", "title": "Internet, Email & Online Safety", "level": "Beginner", "hours": 2,
     "summary": "Search smartly, write professional emails and avoid online fraud.",
     "link": ("Google Digital Garage", "https://learndigital.withgoogle.com/digitalgarage"),
     "lessons": [
        {"t": "Searching well", "body": "Use specific keywords, e.g. 'data entry jobs Mumbai fresher'. Check the website address before trusting a page.", "tip": "Find 3 job openings near you using search."},
        {"t": "Professional email", "body": "Use a simple email address (firstname.lastname). Write a clear subject, greet politely, keep it short, and attach your resume as a PDF.", "tip": "Send a practice email to a friend applying for a job."},
        {"t": "Spotting job scams", "body": "Real companies never ask you to pay money to get a job. Be careful of offers that promise high pay for no work.", "tip": "If it sounds too good to be true, it probably is."}]},
    {"id": "communication", "title": "Communication & Workplace Skills", "level": "Beginner", "hours": 4,
     "summary": "Speak clearly, work in a team and manage your time.",
     "link": ("SWAYAM (Govt. of India)", "https://swayam.gov.in"),
     "lessons": [
        {"t": "Speaking with confidence", "body": "Speak slowly, make eye contact and use simple sentences. Practising in front of a mirror or recording yourself helps a lot.", "tip": "Record a 1-minute introduction about yourself."},
        {"t": "Teamwork", "body": "Listen before replying, share credit, and ask for help early. Teams value people who are reliable.", "tip": "Think of one time you worked in a team and what you learned."},
        {"t": "Time management", "body": "List tasks daily, do the important ones first and avoid last-minute work. Be on time, every time.", "tip": "Plan tomorrow in 5 minutes tonight."}]},
    {"id": "digital-marketing", "title": "Digital Marketing & Freelancing", "level": "Intermediate", "hours": 6,
     "summary": "Use social media and free tools to earn through online work.",
     "link": ("Canva Design School", "https://www.canva.com/learn/"),
     "lessons": [
        {"t": "What is digital marketing?", "body": "Businesses promote products through social media, search engines, email and WhatsApp. Small shops need help with this.", "tip": "Look at how a local shop uses Instagram."},
        {"t": "Design with Canva", "body": "Canva lets you create posters, posts and logos with templates. Good design is simple: few colours, clear text.", "tip": "Create a poster for an imaginary tuition class."},
        {"t": "Starting as a freelancer", "body": "Make a small portfolio of 3 samples, create a profile on a freelance site, and start with small, low-priced projects to build reviews.", "tip": "Offer your first project to a local business for free to get a testimonial."}]},
    {"id": "web-basics", "title": "Web Basics (HTML & CSS)", "level": "Intermediate", "hours": 8,
     "summary": "Build your first web page and discover a path to tech jobs.",
     "link": ("freeCodeCamp", "https://www.freecodecamp.org"),
     "lessons": [
        {"t": "What is HTML?", "body": "HTML gives a page its structure using tags like <h1> for headings and <p> for paragraphs.", "tip": "Create index.html and show your name in an <h1>."},
        {"t": "Styling with CSS", "body": "CSS changes colours, fonts and layout. Example: h1 { color: navy; }", "tip": "Change the background colour of your page."},
        {"t": "Publish your page", "body": "Free hosting sites such as GitHub Pages let you put your page online and share the link in your resume.", "tip": "Add the link to your resume."}]},
]

INTERVIEW = {
    "HR Questions": [
        {"q": "Tell me about yourself.", "tip": "Give 3 parts: who you are, what you studied or learned, and what job you want. Keep it under 1 minute."},
        {"q": "Why should we hire you?", "tip": "Mention 2 skills that match the job and show you are ready to learn."},
        {"q": "What are your strengths and weaknesses?", "tip": "Pick a real strength with an example. For a weakness, share one you are working to improve."},
        {"q": "Where do you see yourself in 5 years?", "tip": "Talk about learning and growing in the company, not about leaving it."},
        {"q": "Why is there a gap in your resume?", "tip": "Be honest and positive. Say what you did to learn, like online courses or helping at home."},
        {"q": "Are you willing to relocate or work in shifts?", "tip": "Answer honestly. If yes, say so clearly; if not, explain politely."}],
    "Basic Computer Skills": [
        {"q": "What is the difference between RAM and storage?", "tip": "RAM is short-term working memory; storage keeps your files permanently."},
        {"q": "How do you create a strong password?", "tip": "Use 12+ characters with letters, numbers and symbols. Do not reuse passwords."},
        {"q": "What is the use of Excel formulas like SUM?", "tip": "Explain that formulas do calculations automatically, saving time and avoiding mistakes."},
        {"q": "How would you attach a file to an email?", "tip": "Click the paperclip icon, choose the file, wait for it to upload, then send."},
        {"q": "What is cloud storage?", "tip": "Online storage like Google Drive that lets you open your files from any device."}],
    "Situation Questions": [
        {"q": "A customer is angry with you. What do you do?", "tip": "Stay calm, listen fully, apologise for the problem, and offer a solution or call a senior."},
        {"q": "You don't know how to do a task given to you. What next?", "tip": "Try first, search or ask a colleague, and tell your manager early if you need help."},
        {"q": "You have two deadlines on the same day. How do you manage?", "tip": "Prioritise by urgency, tell your manager, and plan your time in blocks."},
        {"q": "A teammate is not doing their work. What would you do?", "tip": "Talk to them politely first. If it continues, inform your manager calmly."}],
}

TIPS = [
    "Make a free profile on job portals like Naukri, Indeed and LinkedIn.",
    "Keep your resume to one page and save it as a PDF.",
    "Use a professional email address and a clear phone voicemail.",
    "Check government schemes such as Skill India and the National Career Service (NCS) portal.",
    "Practise your self-introduction until you can say it without reading.",
]
