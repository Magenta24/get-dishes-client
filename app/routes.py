from app import app
from app.forms import InputForm

from flask import render_template

@app.route('/', methods=['GET'])
def home():    
    return render_template("index.html") 

@app.route('/algorithm', methods=['POST'])
def home():    
    return "OK"