from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, DateTimeLocalField, SelectField
from wtforms.validators import DataRequired, Length


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
