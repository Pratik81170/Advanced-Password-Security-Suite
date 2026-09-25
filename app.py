from flask import Flask, render_template, request,send_file
from reportlab.pdfgen import canvas
from password_engine import generate_password, analyze_password

app = Flask(__name__)

password_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        generated_password="",
        analysis=None,
        selected_length=16,
        history=password_history
    )


@app.route("/generate", methods=["POST"])
def generate():

    length = int(request.form.get("length", 16))

    uppercase = request.form.get("uppercase") == "on"
    lowercase = request.form.get("lowercase") == "on"
    numbers = request.form.get("numbers") == "on"
    symbols = request.form.get("symbols") == "on"

    password = generate_password(
        length,
        uppercase,
        lowercase,
        numbers,
        symbols
    )
    password_history.insert(0, password)

    if len(password_history) > 5:
       password_history.pop()

    return render_template(
        "dashboard.html",
         generated_password=password,
        analysis=None,
        selected_length=length,
        history=password_history
    )
      


@app.route("/analyze", methods=["POST"])
def analyze():

    password = request.form.get("password")

    report = analyze_password(password)

    return render_template(
        "dashboard.html",
        generated_password="",
        analysis=report,
        selected_length=16,
        history=password_history
    )
@app.route("/download_pdf")
def download_pdf():
    pdf_file = "password_report.pdf"

    c = canvas.Canvas(pdf_file)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "Password Security Report")

    c.setFont("Helvetica", 12)
    c.drawString(100, 760, f"Generated Passwords: {len(password_history)}")

    y = 730
    for i, pwd in enumerate(password_history, 1):
        c.drawString(100, y, f"{i}. {pwd}")
        y -= 20

    c.save()

    return send_file(pdf_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True,port=5001)