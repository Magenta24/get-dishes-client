from app import app
from app.forms import InputForm
from flask import render_template, request
from config import GRAPH_SERVICE_URL
import requests


@app.route('/', methods=['GET', 'POST'])
def home():    
    form = InputForm(['xd', 'xxd', 'xddd', 'xdxdxdx'])
    return render_template("index.html", form=form) 

@app.route('/algorithm', methods=['POST'])
def algorithm():    
    algorithm = request.get("algorithm", default="")
    nodes = request.get("nodes", default=[])
    edges = request.get("nodes", default=[])
    bidirectional = request.get("bidirectional", default=False, type=None)

    response = requests.get(GRAPH_SERVICE_URL + "/algorithm")