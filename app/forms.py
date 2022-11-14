from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.fields import SelectField
from wtforms.fields.simple import  SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    algorithms = SelectField('Algorithm', choices = [],  validators = [DataRequired()])
    vertices = StringField('Vertices', validators = [DataRequired()])
    edges = StringField('Edges', validators = [DataRequired()])
    bidirectional = BooleanField('Bidirectional')

    submit = SubmitField('Submit')

    def __init__(self, algorithm_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.algorithms.choices = algorithm_choices
