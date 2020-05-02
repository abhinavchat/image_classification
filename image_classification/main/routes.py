from image_classification.main import main
from flask import render_template, url_for
from flask_login import login_required
from image_classification.main.forms import PredictionForm
from .util import image_to_numpy, get_prediction

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
        npimg = image_to_numpy(form.image.data)
        print(type(npimg))
        prediction = get_prediction(npimg)
        print(f"PREDICTION: {prediction}")
        return render_template('prediction.html', form=form, prediction=prediction)

    return render_template('prediction.html', form=form)