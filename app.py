from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("beard.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/appointment")
def appointment():
    return render_template("appointment.html")


if __name__ == "__main__":
    app.run(debug=True)
