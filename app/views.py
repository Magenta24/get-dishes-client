from app import app
from forms import InputForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = InputForm()


    if form.validate_on_submit():
        pass
    
    return "hello world" 

