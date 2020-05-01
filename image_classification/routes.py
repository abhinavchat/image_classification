from flask import render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from image_classification import app
from image_classification.forms import LoginForm
from image_classification.models import User

@app.route('/')
@app.route('/home')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('You have successfully logged in!')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username or password.')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    pass

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))