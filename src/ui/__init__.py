

from flask import Flask

app = Flask(__name__)

from . import routes
app.static_folder = 'static'
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 