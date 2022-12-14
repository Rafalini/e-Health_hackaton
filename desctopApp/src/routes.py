import os
import pandas as pd

from sqlalchemy import desc

from src.functions import save_profile_picture
from flask import render_template, url_for, flash, redirect, request

from src import app, db, bcrypt
from src.forms import DoctorRegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm
from src.dbmodels import Announcement, Patient, Result
from flask_login import login_user, current_user, logout_user, login_required

db.create_all()


@app.route("/")
@app.route("/home")
def home():
    patients = Patient.query.all()
    data = []
    iter = 0
    for patinet in patients:
        iter += 1
        res = Result.query.filter_by(user_id=patinet.id).first()
        if res is not None:
            res.number = iter
            data.append(res)
    return render_template('home.html', results=data)


@app.route("/ekg/<int:ekg_id>")
def ekg(ekg_id):
    result = Result.query.get_or_404(ekg_id)
    df = pd.read_csv(os.getcwd()+"/src/data/ekg_"+str(ekg_id)+".csv", encoding='L7')
    return render_template('ekgPopOut.html', time=df.time.tolist(), hr=df.hr.tolist(), result=result, display=False)

@app.route("/hr/<int:hr_id>")
def hr(hr_id):
    result = Result.query.get_or_404(hr_id)
    df = pd.read_csv(os.getcwd()+"/src/data/hr_"+str(hr_id)+".csv", encoding='L7')
    return render_template('heartRate.html', time=df.time.tolist(), hr=df.hr.tolist(), result=result, display=False)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = DoctorRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Patient(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Patient.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            print(current_user.is_authenticated)
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Zaloguj si??', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            current_user.image_file = save_profile_picture(form.picture.data)
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phone.data = current_user.phone
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/announcements")
def announcements():
    return render_template('announcements.html', announcements=Announcement.query.all())


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # flash(send_reset_email(user), 'info')
        return redirect(url_for('login'))
    return render_template('resetRequest.html', title='Reset Password', form=form)
