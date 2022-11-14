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