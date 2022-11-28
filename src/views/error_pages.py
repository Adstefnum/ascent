from src import app
from flask import render_template

def error_view(message):
    
    return render_template('error_pages.html', message=message)