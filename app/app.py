from flask import Flask, render_template, request, redirect, url_for
import os  # Required for file handling

app = Flask(__name__)

# Configuration for uploads
app.config["UPLOAD_FOLDER"] = "static/uploads/"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}

# Function to check if a file is allowed
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/", methods=["GET", "POST"])
def home():
    print("[INFO] Rendering the home page")
    submitted_contact_info = None  # Initialize variable to store contact form data

    # Handle contact form submission
    if request.method == "POST" and "name" in request.form:
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Validate contact form data
        if name and email and message:
            submitted_contact_info = {"name": name, "email": email, "message": message}
            print(f"[INFO] Contact form submitted: {submitted_contact_info}")
        else:
            return "All fields in the contact form are required."

    # Render the home page and pass the submitted contact info
    return render_template("home.html", contact_info=submitted_contact_info)

@app.route("/upload", methods=["POST"])
def upload_file():
    # Handle file upload
    if "image" not in request.files:
        return "No file part in the request."
    file = request.files["image"]
    if file.filename == "":
        return "No file selected."
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        try:
            os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)  # Ensure the upload folder exists
            file.save(filepath)
            print(f"[INFO] File successfully uploaded to {filepath}")
            return f"File successfully uploaded to: {filepath}"
        except Exception as e:
            print(f"[ERROR] Failed to save file: {e}")
            return "An error occurred while saving the file."
    return "File upload failed."

@app.route("/about")
def about():
    print("[INFO] Rendering the about page")
    try:
        return render_template("about.html")
    except Exception as e:
        print(f"[ERROR] Failed to render about.html: {e}")
        return "Error loading the About Page."

@app.route("/portfolio")
def portfolio():
    print("[INFO] Rendering the portfolio page")
    try:
        return render_template("portfolio.html")
    except Exception as e:
        print(f"[ERROR] Failed to render portfolio.html: {e}")
        return "Error loading the Portfolio Page."

@app.route("/images")
def images():
    print("[INFO] Rendering the images page")
    try:
        return render_template("images.html")
    except Exception as e:
        print(f"[ERROR] Failed to render images.html: {e}")
        return "Error loading the Images Page."

if __name__ == "__main__":
    print("[INFO] Starting the Flask application...")
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        print(f"[ERROR] Failed to start the Flask application: {e}")
