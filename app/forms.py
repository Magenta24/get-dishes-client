from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.fields import SelectField
from wtforms.fields.simple import  SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    category1 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient1 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    ingredients = StringField('Edges', validators = [DataRequired()])

    submit = SubmitField('Submit')

    def __init__(self, ingredient_categories, ingredients, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category1.choices = ingredient_categories
        self.ingredient1.choices = ingredients
