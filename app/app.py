from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print("Home route accessed")
    return render_template("home.html")

@app.route("/about")
def about():
    print("About route accessed")
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    print("Portfolio route accessed")
    return render_template("portfolio.html")

@app.route("/images")
def images():
    print("Images route accessed")
    return render_template("images.html")

if __name__ == "__main__":
    print("Starting Flask application with debug mode enabled...")
    app.run(host="0.0.0.0", port=5000, debug=True)  # Debug mode ON
