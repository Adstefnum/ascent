

from flask import Flask, session
from flask_cors import CORS
from flask_session import Session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

from . import routes
app.static_folder = 'static'
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

csrf = CSRFProtect()
Session(app)
CORS(app)

@app.template_filter('caps')
def reverse_filter(string:str):
    return string.upper()

