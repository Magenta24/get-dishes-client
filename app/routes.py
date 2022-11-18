from app import app
from app.forms import InputForm
from flask import render_template, request
from config import GRAPH_SERVICE_URL, SERVICE1_URL
import requests
import json


@app.route('/', methods=['GET', 'POST'])
def home():    

    # getting all categories
    json_categories = requests.get(SERVICE1_URL + '/ingredient_categories')
    categories_names = ['...']
    ingredients = ['...']
    
    for c in json_categories.json()['categories']:
        categories_names.append(c['name'])
        
    form = InputForm(categories_names, ingredients)

    # getting response from service with dishes containing user's ingredients
    if request.method == 'POST':
        user_ingredients = {}

        for i in range(1, 10):
            user_ingredients['ingredient' + str(i)] = request.form.get('ingredient' + str(i))

        print(user_ingredients)
        dishes_response = requests.get(SERVICE1_URL + '/Dishes?', data=user_ingredients)
        return dishes_response.json()

    return render_template("index.html", form=form) 

# returns json with ingredients with given category
@app.route('/ingredients/<category>')
def ingredients(category):
    pass

# returns all dishes matching the user's selected ingredients  
@app.route('/check_dishes', methods=[])
def check_dishes():
    pass

@app.route('/recipie', methods=['POST'])
def algorithm():    
    algorithm = request.args.get("algorithm", default="")
    nodes = request.args.get("nodes", default=[])
    edges = request.args.get("nodes", default=[])
    bidirectional = request.args.get("bidirectional", default=False, type=None)

    response = requests.post(GRAPH_SERVICE_URL + "/algorithm?", data={
        "algorithm": algorithm,
        "nodes": nodes,
        "edges": edges,
        "bidirectional": bidirectional
    })

    # Some magic I will do Here :P

    print(response.json)