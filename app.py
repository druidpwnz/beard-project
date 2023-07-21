# TODO generate content for site with chatgpt
# TODO add flask-login for login into admin page
# TODO add feedback page and feedback form
# TODO move models, forms and views to different modules

from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, DateTimeLocalField, SelectField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///beard.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# TODO add Services Choice to table and form
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    service_choice = db.Column(db.String)
    convenient_time = db.Column(db.DateTime)


class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=30)])
    email = EmailField("Email", validators=[DataRequired()])
    phone = TelField("Phone", validators=[DataRequired()])
    service_choice = SelectField(
        "Service Choice",
        validators=[DataRequired()],
        choices=["Hair Cut", "Beard Cut", "Facial Pack"],
    )
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
        service_choice = form.service_choice.data
        convenient_time = form.convenient_time.data

        new_appointment = Appointment(
            name=name,
            email=email,
            phone=phone,
            service_choice=service_choice,
            convenient_time=convenient_time,
        )
        db.session.add(new_appointment)
        db.session.commit()

        return redirect(url_for("success_appointment", name=name, time=convenient_time))

    return render_template("appointment.html", form=form)


@app.route("/success_appointment/<name>/<time>")
def success_appointment(name, time):
    return render_template("success_appointment.html", name=name, time=time)


@app.route("/admin")
def admin():
    appointments = Appointment.query.order_by(Appointment.id.desc()).all()

    return render_template("admin.html", appointments=appointments)


if __name__ == "__main__":
    app.run(debug=True)
