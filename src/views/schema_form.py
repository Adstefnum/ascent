from .json_to_sql.json_to_sql import json_to_sql_upload
from flask import request, render_template
import ujson

conn_data_global = {}

def schema_form_get(conn_data):
    global conn_data_global
    conn_data_global = ujson.loads(str(conn_data))
    print(conn_data_global)

    return render_template('layouts/schema_form.html')

def schema_form_post():

    if request.method =="POST":
        schema = request.form.to_dict()
        print(schema)
        conn_data_global.update(schema)
        return json_to_sql_upload(conn_data_global)
