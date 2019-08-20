from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    preferred_name = StringField('Preferred Name')


class LogInForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
