from flask import render_template, redirect, url_for, flash
from image_classification import app
from image_classification.forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "password":
            flash('You have successfully logged in!')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username or password.')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    pass