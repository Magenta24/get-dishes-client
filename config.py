import os
from pathlib import Path
# Enabling CSRF protection
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key-1234-#$%^'

# setting prject's base directory
basedir = os.path.abspath(os.path.dirname(__file__))

SERVICE1_URL = 'http://127.0.0.1:5000'

SERVICE_2_URL = 'http://localhost:8080/api'

API_KEY = '4nohXYsTp0V8_-JhC5JHP0-Eg0VSU6iCraaWkQK3yqXD'
IBM_URL = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/50f3a644-4baf-4860-a6c9-8f97f35d3016'

TTS_FOLDER = Path(basedir, "tts")

DEFAULT_IMAGE_PATH = "images/no_image_burger.png"