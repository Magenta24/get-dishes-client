import os
from pathlib import Path
# Enabling CSRF protection
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key-1234-#$%^'

# setting prject's base directory
basedir = os.path.abspath(os.path.dirname(__file__))

SERVICE1_URL = 'http://127.0.0.1:5000'
SERVICE_2_URL = 'http://localhost:8080/api'

API_KEY = 'zYAH4XzJ_X6U-RetmZw-Y0-1L2a8uG_qrE5MTKzM7-SM'
IBM_URL = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/a02d1a2d-2e39-42af-871e-3e8007f2e5e3'

TTS_FOLDER = Path(basedir, "tts/")

DEFAULT_IMAGE_PATH = "images/no_image_burger.png"