from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, DateTimeLocalField
from wtforms.validators import DataRequired, Length
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)


class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=30)])
    email = EmailField("Email", validators=[DataRequired()])
    phone = TelField("Phone", validators=[DataRequired()])
    convenient_time = DateTimeLocalField(
        "Convenient Time", validators=[DataRequired()], format="%Y-%m-%dT%H:%M"
    )


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


@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    form = AppointmentForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        convenient_time = form.convenient_time.data

        return f"<h1>Name {name}, Email {email}, Phone {phone}, Convenient time {convenient_time}</h1>"

    return render_template("appointment.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
