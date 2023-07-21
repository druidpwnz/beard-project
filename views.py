from flask import redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from app import app, db, login_manager
from models import Appointment, User
from forms import AppointmentForm, LoginForm
from werkzeug.security import check_password_hash

login_manager.login_view = "login"
login_manager.login_message = "You cannot access that page. You need to login first."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if not user:
            return render_template(
                "login.html", form=form, message="User does not exist"
            )

        if check_password_hash(user.password, password):
            login_user(user)

            return redirect(url_for("admin"))

        return render_template("login.html", form=form, message="Password is wrong")

    return render_template("login.html", form=form)


@app.route("/admin")
@login_required
def admin():
    appointments = Appointment.query.order_by(Appointment.id.desc()).all()

    return render_template("admin.html", appointments=appointments)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
