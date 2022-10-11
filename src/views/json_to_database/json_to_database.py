from flask import render_template
from forms.json_to_database import JsonToDatabaseForm

def json_to_database():
    form = JsonToDatabaseForm()
    return render_template('json_to_database/index.html',file_ext="json",form=form)