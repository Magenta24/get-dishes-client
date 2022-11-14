from datetime import datetime, timedelta
import hashlib
from flask.globals import session
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, HiddenField, \
    BooleanField, DateField, IntegerField, TimeField, RadioField
from wtforms.fields import SelectField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo, Email, NumberRange
from wtforms.widgets.core import TextArea

import re

from app.models import Discount, Location, PricingModel, User, UserDiscount
from config import HASH, HASH_ITERATION

def password_check(form, field):
    password = form.password.data
    if re.search('[0-9]', password) is None:
        raise ValidationError('Password must contain a number')
    elif re.search('[A-Z]', password) is None:
        raise ValidationError('Password must have one uppercase letter')

def username_check(form, field):
    username = form.username.data
    if User.query.filter_by(username=username).first() is not None:
        raise ValidationError('User with this username already exits')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators = [
        DataRequired(),
        username_check
        ])
    password = PasswordField('Password', validators = [
        DataRequired(),
        password_check,
        Length(min = 8, max = 40, message = "password between 8 and 40 characters"),
        EqualTo('confirm', message = 'Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')    
    firstname = StringField('First Name', validators = [
        DataRequired(),
    ])

    email = EmailField('Email', validators = [
        DataRequired(),
        Email()
    ])
    phone_number = StringField('Phone Number')
    
    surname = StringField('Surname', validators = [
        DataRequired(),
    ])
    submit = SubmitField('Register')


class InputForm(FlaskForm):
    algorithms = SelectField('Algorithm', choices = [],  validators = [DataRequired()])
    vertices = StringField('Vertices', validators = [DataRequired()])
    edges = StringField('Edges', validators = [DataRequired()])
    bidirectional = BooleanField('Bidirectional')

    submit = SubmitField('Submit')

    def __init__(self, algorithm_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.algorithms.choices = algorithm_choices
