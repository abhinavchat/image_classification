from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms.fields import StringField, PasswordField, SubmitField
from image_classification.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Password and Confirm Password must be equal")])
    submit = SubmitField('Signup')

    def validate_username(self, username):
        u = User.query.filter_by(username=username.data).first()
        if u:
            raise ValidationError(f"Username {username.data} already taken.")

    def validate_email(self, email):
        u = User.query.filter_by(email=email.data).first()
        if u:
            raise ValidationError(f"Email Address {email.data} already in use.")