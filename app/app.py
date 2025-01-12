from flask import Flask, render_template, request
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv  # For secure environment variables

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Function to send email
def send_email(student_name, student_id, slot):
    sender_email = os.getenv("EMAIL_ADDRESS")  # Load from .env
    sender_password = os.getenv("EMAIL_PASSWORD")  # Load from .env
    recipient_email = os.getenv("RECIPIENT_EMAIL")  # Notification email

    if not sender_email or not sender_password or not recipient_email:
        print("[ERROR] Email credentials are not set.")
        return

    subject = "New Appointment has been completed onyl one the 1"
    body = f"""
    Hello {student_name},
    Your appointment has been successfully booked:
    - Name: {student_name}
    - Student ID: {student_id}
    - Slot: {slot}
    Thank you!
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("[INFO] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

# Appointments dictionary
appointments = {"Sunday 9:00 AM - 10:00 AM": [], "Tuesday 9:00 AM - 10:00 AM": []}

@app.route("/appointments", methods=["GET", "POST"])
def appointments_page():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        student_id = request.form.get("student_id")
        slot = request.form.get("slot")

        if name and student_id and slot:
            if len(appointments[slot]) < 3:
                appointments[slot].append({"name": name, "student_id": student_id})
                message = f"Appointment confirmed for {slot}."
                send_email(name, student_id, slot)
            else:
                message = f"{slot} is full. Please choose another slot."
        else:
            message = "All fields are required."

    return render_template("appointments.html", appointments=appointments, message=message)

@app.route("/")
def home():
    print("[INFO] Rendering the home page")
    return render_template("home.html")

@app.route("/about")
def about():
    print("[INFO] Rendering the about page")
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    print("[INFO] Rendering the portfolio page")
    return render_template("portfolio.html")

@app.route("/images")
def images():
    print("[INFO] Rendering the images page")
    return render_template("images.html")

if __name__ == "__main__":
    print("[INFO] Starting the Flask application...")
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        print(f"[ERROR] Failed to start the Flask application: {e}")
