

from flask import Flask, session
from flask_cors import CORS
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

from . import routes
app.static_folder = 'static'
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOADS_FOLDER")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'

CSRFProtect(app)
Session(app)
CORS(app)

@app.template_filter('caps')
def reverse_filter(string:str):
    return string.upper()

