from image_classification.main import main
from flask import render_template
from flask_login import login_required

@main.route('/')
@main.route('/home')
@login_required
def index():
    return render_template('index.html')