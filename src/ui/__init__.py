

from flask import Flask

app = Flask(__name__)

from . import routes
app.static_folder = 'static'
