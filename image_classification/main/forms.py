from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms.fields import StringField, PasswordField, SubmitField


class PredictionForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired()])
    submit = SubmitField('Predict')