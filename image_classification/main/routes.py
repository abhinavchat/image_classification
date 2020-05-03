from image_classification.main import main
from flask import render_template, url_for, current_app, send_file, redirect
from flask_login import login_required
from image_classification.main.forms import PredictionForm
from .util import image_to_numpy, get_prediction
import base64
from werkzeug.utils import secure_filename

@main.route('/')
@main.route('/home')
@login_required
def index():
    return render_template('index.html')

@main.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    form = PredictionForm()
    if form.validate_on_submit():
        import os
        f = form.image.data
        print(f"Changing {f.filename} to {secure_filename(f.filename)}")
        print(f"Image Data: {f}")
        print(f"Image: {form.image}")
        f.save(os.path.join(current_app.config["FILE_UPLOAD_PATH"], secure_filename(f.filename)))
        npimg = image_to_numpy(os.path.join(current_app.config["FILE_UPLOAD_PATH"], secure_filename(f.filename)))
        print(type(npimg))
        prediction = get_prediction(npimg)
        print(f"PREDICTION: {prediction}")
        return render_template('prediction.html', form=form, prediction=prediction, filename=secure_filename(f.filename))

    return render_template('prediction.html', form=form)

@main.route('/display/<filename>')
@login_required
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)