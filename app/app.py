from flask import Flask, render_template, request
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv  # For loading environment variables securely

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Function to send email
def send_email(student_name, student_id, slot):
    # Get email credentials from environment variables
    sender_email = os.getenv("EMAIL_ADDRESS")  # Sender's email address
    sender_password = os.getenv("EMAIL_PASSWORD")  # Sender's email password
    recipient_email = os.getenv("RECIPIENT_EMAIL")  # Recipient's email address for notifications

    # Check if email credentials are set
    if not sender_email or not sender_password or not recipient_email:
        print("[ERROR] Email credentials are not set.")
        return

    # Email subject and body
    subject = "New Appointment Confirmation"
    body = f"""
    Hello {student_name},
    Your appointment has been successfully booked:
    - Name: {student_name}
    - Student ID: {student_id}
    - Slot: {slot}
    Thank you!
    """

    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))  # Attach the email body

    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email message
            print("[INFO] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

# Appointments dictionary to store booked appointments
appointments = {
    "Sunday 9:00 AM - 10:00 AM": [],
    "Tuesday 9:00 AM - 10:00 AM": []
}

@app.route("/appointments", methods=["GET", "POST"])
def appointments_page():
    message = ""  # Initialize message variable
    if request.method == "POST":  # Check if the request method is POST
        name = request.form.get("name")  # Get the name from the form
        student_id = request.form.get("student_id")  # Get the student ID from the form
        slot = request.form.get("slot")  # Get the selected time slot from the form

        # Check if all fields are filled
        if name and student_id and slot:
            # Check if the selected slot has less than 3 appointments
            if len(appointments[slot]) < 3:
                appointments[slot].append({"name": name, "student_id": student_id})  # Add appointment
                message = f"Appointment confirmed for {slot}."  # Confirmation message
                send_email(name, student_id, slot)  # Send confirmation email
            else:
                message = f"{slot} is full. Please choose another slot."  # Slot full message
        else:
            message = "All fields are required."  # Error message for missing fields

    # Render the appointments page with the current appointments and message
    return render_template("appointments.html", appointments=appointments, message=message)

@app.route("/")
def home():
    print("[INFO] Rendering the home page")
    return render_template("home.html")  # Render the home page

@app.route("/about")
def about():
    print("[INFO] Rendering the about page")
    return render_template("about.html")  # Render the about page

@app.route("/portfolio")
def portfolio():
    print("[INFO] Rendering the portfolio page")
    return render_template("portfolio.html")  # Render the portfolio page

@app.route("/images")
def images():
    print("[INFO] Rendering the images page")
    return render_template("images.html")  # Render the images page

if __name__ == "__main__":
    print("[INFO] Starting the Flask application...")
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)  # Start the Flask application
    except Exception as e:
        print(f"[ERROR] Failed to start the Flask application: {e}") 