from .json_to_sql.json_to_sql import json_to_sql_upload
from flask import request, render_template, url_for, redirect
import ujson
from src.forms.schema import SchemaForm

conn_data_global = {}
global_form = SchemaForm()

def schema_form_get(conn_data):
    global conn_data_global
    conn_data_global = ujson.loads(str(conn_data))
    print(conn_data_global)

    form = SchemaForm()
    global_form = form

    return render_template('layouts/schema_form.html',form=form)

def schema_form_post():

    if request.method =="POST" and global_form.validate():
        schema = request.form.to_dict()
        print(schema)
        conn_data_global.update(schema)
        return json_to_sql_upload(conn_data_global)

    return redirect(url_for('json_to_sql'))
