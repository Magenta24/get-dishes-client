from app import app
from app.forms import InputForm
from flask import render_template, request
from config import GRAPH_SERVICE_URL
import requests
import json


@app.route('/', methods=['GET', 'POST'])
def home():    
    json_categories = requests.get('http://127.0.0.1:5000/ingredient_categories')
    categories_names = []
    ingredients = []
    
    for c in json_categories.json():
        categories_names.append(json_categories.json()[c]['name'])

    json_ingredients = requests.get('http://127.0.0.1:5000/ingredients/' + json_categories.json()['1']['name'])

    for i in json_ingredients.json()['ingredients']:
        ingredients.append(i['name'])
        
    form = InputForm(categories_names, ingredients)

    if request.method == 'POST':
        return form.category1.data
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