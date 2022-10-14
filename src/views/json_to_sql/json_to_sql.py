from flask import render_template,request,Response, redirect, url_for
from forms.json_to_sql import JsonToDatabaseForm
from utils.dbutils import get_connection
from utils.file_upload_utils import user_upload_file
import os
from src import app
import ujson

def json_to_sql():
    form = JsonToDatabaseForm()

    if request.method =="POST" and form.validate():
        data = request.form.to_dict()
        user_upload_file("json")
        return json_to_sql_upload(data)

    return render_template('json_to_sql/index.html',file_ext="json",form=form)

#redirect to this page and show data concerning upload
def json_to_sql_upload(data):
    
    conn = get_connection(data)
    cur = conn.cursor()
    count = 100
    number = 0
    status="uploading"
    transactions = []

    create_table_sql = f"""
    use {data["dbname"]}
    DROP IF EXISTS {data["table_name"]};
    CREATE TABLE {data["table_name"]}
        {data["schema"]};
    """

    insert_sql = f"""
         
    use {data["dbname"]}
        """ 



    file = os.path.join(app.config["UPLOAD_FOLDER"], "upload.json")
    
    with open(file, 'r') as f:
        data = ujson.dumps(f.read())




    return render_template('json_to_sql/upload.html',count=count,number=number,status=status)
