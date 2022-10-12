from flask import render_template
from forms.json_to_sql import JsonToDatabaseForm

def json_to_sql():
    form = JsonToDatabaseForm()
    form.validate()
    #after validation then I need to connect to the database, start processing the json into 
    #transactions and then upload at once.
    return render_template('json_to_sql/index.html',file_ext="json",form=form)