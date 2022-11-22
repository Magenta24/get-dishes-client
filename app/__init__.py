from flask import Flask
from config import TTS_FOLDER
import os

app = Flask(__name__)

app.config.from_object('config')

if not os.path.exists(TTS_FOLDER):
    os.mkdir(TTS_FOLDER)

from app import routes
