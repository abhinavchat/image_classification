from image_classification.auth import auth
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from image_classification.auth.forms import LoginForm
from image_classification.models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('You have successfully logged in!')
            return redirect(url_for('main.index'))
        else:
            flash('Incorrect username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    pass

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))