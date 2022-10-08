from datetime import datetime
from src import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_doctor(user_id):
    return Patient.query.get(int(user_id))


class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    patients = db.relationship('Patient', backref='doctorId', lazy=True)

    def __repr__(self):
        return f"Doctor('{self.id}', '{self.username}', '{self.email}', '{self.image_file}')"


class Patient(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    parentDoctor = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=True)
    medicalResults = db.relationship('Result', backref='owner', lazy=True)

    def __repr__(self):
        return f"Patient('{self.id}', '{self.username}', '{self.email}', '{self.image_file}')"


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=True)

    def __repr__(self):
        return f"Result('{self.id}', '{self.title}', '{self.user_id}')"


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=True)
