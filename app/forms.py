from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.fields import SelectField
from wtforms.fields.simple import  SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    category1 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient1 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category2 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient2 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category3 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient3 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category4 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient4 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category5 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient5 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category6 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient6 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category7 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient7 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category8 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient8 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category9 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient9 = SelectField('Ingredient', choices = [], validators = [DataRequired()])
    
    category10 = SelectField('Category', choices = [],  validators = [DataRequired()])
    ingredient10 = SelectField('Ingredient', choices = [], validators = [DataRequired()])

    submit = SubmitField('Submit')

    def __init__(self, ingredient_categories, ingredients, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category1.choices = ingredient_categories
        self.ingredient1.choices = ingredients
        self.category2.choices = ingredient_categories
        self.ingredient2.choices = ingredients
        self.category3.choices = ingredient_categories
        self.ingredient3.choices = ingredients
        self.category4.choices = ingredient_categories
        self.ingredient4.choices = ingredients
        self.category5.choices = ingredient_categories
        self.ingredient5.choices = ingredients
        self.category6.choices = ingredient_categories
        self.ingredient6.choices = ingredients
        self.category7.choices = ingredient_categories
        self.ingredient7.choices = ingredients
        self.category8.choices = ingredient_categories
        self.ingredient8.choices = ingredients
        self.category9.choices = ingredient_categories
        self.ingredient9.choices = ingredients
        self.category10.choices = ingredient_categories
        self.ingredient10.choices = ingredients

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])

    submit = SubmitField('Log In')
