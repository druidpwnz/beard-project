from app import db


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    service_choice = db.Column(db.String)
    convenient_time = db.Column(db.DateTime)
