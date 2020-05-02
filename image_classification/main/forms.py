from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms.fields import StringField, PasswordField, SubmitField, FileField


class PredictionForm(FlaskForm):
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Predict')