from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print("Rendering the home page")
    return render_template("home.html")

@app.route("/about")
def about():
    print("Rendering the about page")
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    print("Rendering the portfolio page")
    return render_template("portfolio.html")

@app.route("/images")
def images():
    print("Rendering the images page")
    return render_template("images.html")

if __name__ == "__main__":
    print("Starting the Flask application...")
    app.run(host="0.0.0.0", port=5000)
