from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.static_folder = 'static'

def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))