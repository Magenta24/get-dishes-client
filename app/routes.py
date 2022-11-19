from app import app
from app.forms import InputForm
from flask import render_template, request
from config import SERVICE1_URL, SERVICE_2_URL
import requests


@app.route('/', methods=['GET', 'POST'])
def home():    

    # getting all categories
    json_categories = requests.get(SERVICE1_URL + '/ingredient_categories')
    categories_names = ['...']
    ingredients = ['...']
    print(json_categories)
    
    for c in json_categories.json()['categories']:
        categories_names.append(c['name'])
        
    form = InputForm(categories_names, ingredients)

    # getting response from service with dishes containing user's ingredients

    return render_template("index.html", form=form) 

# returns json with ingredients with given category
@app.route('/ingredients/<category>')
def ingredients(category):
    pass

# returns all dishes matching the user's selected ingredients  
@app.route('/check_dishes', methods=['POST'])
def check_dishes():
    user_ingredients = {}

    for i in range(1, 11):
        user_ingredients['ingredient' + str(i)] = request.form.get('ingredient' + str(i))

    print(user_ingredients)

    dishes_response = requests.post(SERVICE1_URL + '/dishes', json=user_ingredients)

    dishes_and_recipes = {}

    for dish in dishes_response:
        print(dish, type(dish))
        print(SERVICE_2_URL + f'/dish/{str(dish)}')
        post_recipes = requests.get(SERVICE_2_URL + f'/dish/{str(dish)}')
        print(post_recipes)
        recipes = post_recipes.json()
        if len(recipes) > 0:
            dishes_and_recipes[str(dish)]['recipe'] = recipes[0]['recipe']
            if 'imageName' in recipes[0].keys():
                dishes_and_recipes[str(dish)]['image_url'] = SERVICE_2_URL + "/downloadFile/" + recipes[0].get('imageName')
            else:
                dishes_and_recipes[str(dish)]['image_url'] = "DEFAULT_IMAGE_PATH"

    print(dishes_and_recipes)
    return dishes_and_recipes
