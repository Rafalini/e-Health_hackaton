from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DecimalField
from wtforms.validators import *
from src.dbmodels import Doctor, Patient


class DoctorRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if Doctor.query.filter_by(username=username.data).first():
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if Doctor.query.filter_by(email=email.data).first():
            raise ValidationError('That email is taken. Please choose a different one.')


class PatientRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if Patient.query.filter_by(username=username.data).first():
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if Patient.query.filter_by(email=email.data).first():
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Imię i nazwisko', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Numer telefonu', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = Patient.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Patient.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    latitude = DecimalField('Latitude', validators=[Optional(), NumberRange(0, 90, 'wrong number')])
    longitude = DecimalField('Longitude', validators=[Optional(), NumberRange(0, 90, 'wrong number')])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Post image', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = Patient.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')