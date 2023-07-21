from flask import redirect, render_template, url_for
from app import app, db
from models import Appointment
from forms import AppointmentForm


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
