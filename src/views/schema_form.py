from .json_to_sql.json_to_sql import json_to_sql_upload
from flask import request, render_template

def schema_form():

    conn_data=request.args.get("conn_data")
    if request.method =="POST":
        print(conn_data)
#        schema = request.form.to_dict()
        schema = request.args()
        print(schema)
        conn_data["schema"] = schema
        print(conn_data)
        return json_to_sql_upload(conn_data)

    return render_template('layouts/schema_form.html')
