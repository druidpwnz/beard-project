from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TelField,
    EmailField,
    DateTimeLocalField,
    SelectField,
    PasswordField,
    TextAreaField,
)
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


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=20)]
    )
    password = PasswordField(validators=[DataRequired(), Length(min=5, max=50)])


class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=30)])
    feedback_text = TextAreaField("Feedback Text", validators=[DataRequired()])
