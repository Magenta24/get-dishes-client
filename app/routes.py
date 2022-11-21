from app import app
from app.forms import InputForm
from flask import render_template, request, send_from_directory
from config import API_KEY, DEFAULT_IMAGE_PATH, IBM_URL, SERVICE1_URL, SERVICE_2_URL, TTS_FOLDER
import requests
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator(API_KEY)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(IBM_URL)


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

    print(dishes_and_recipes)
    print(dishes_response.json())

    print("I HARDCODED THE EXAMPLES PLEASE REMOVE MEEEEEEEEEEEEEEEEEEEEEE")
    HARDCODED_EXAMPLE = ['spaghetti']

    for dish in HARDCODED_EXAMPLE:
    # for dish in dishes_response.json():
        post_recipes = requests.get(SERVICE_2_URL + f'/dishes/{str(dish)}')

        recipes = post_recipes.json()
        if len(recipes) > 0:
            if str(dish) not in dishes_and_recipes.keys():
                dishes_and_recipes[str(dish)] = dict()

            dishes_and_recipes[str(dish)]['recipe'] = recipes[0]['recipe']
            if 'imageName' in recipes[0].keys():
                dishes_and_recipes[str(dish)]['image_url'] = SERVICE_2_URL + "/downloadFile/" + recipes[0].get('imageName')
            else:
                dishes_and_recipes[str(dish)]['image_url'] = DEFAULT_IMAGE_PATH

            # with open(f'{TTS_FOLDER}{dish}.mp3', 'wb') as audio_file:
            #     audio_file.write(
            #         text_to_speech.synthesize(
            #             recipes[0]['recipe'],
            #             voice='en-US_AllisonV3Voice',
            #             accept='audio/mp3'        
            #         ).get_result().content)
    print(dishes_and_recipes)
    return render_template("dishes.html", dishes = dishes_and_recipes)


@app.route('/get_recipe_audio/<string:dish_name>')
def get_recipe_audio(dish_name):
    return send_from_directory(TTS_FOLDER, f'{dish_name}.mp3', as_attachment=True)