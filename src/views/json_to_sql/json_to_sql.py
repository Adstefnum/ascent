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
        data=ujson.dumps(data)
        print(data)
        user_upload_file("json")
        return redirect(url_for('schema_form_get',conn_data=data))

    return render_template('json_to_sql/index.html',file_ext="json",form=form)

#redirect to this page and show data concerning upload
def json_to_sql_upload(data):
    print(data)

    conn = get_connection(data)
    cur = conn.cursor()
    count = 100
    number = 0
    status="uploading"

    json_ready_schema = ""
    for col in data["schema"]:
        tokens = col.split(" ")
        qualifiers = " ".join(tokens[1:])
        json_ready_schema += f"`{tokens[0]}` {qualifiers} AS (JSON_VALUE(json_data, '$.{tokens[0]}')) VIRTUAL,\n"

    create_table_sql = f"""
    use {data["dbname"]}
    DROP IF EXISTS {data["table_name"]};
    CREATE TABLE {data["table_name"]}
        {data["schema"]}
        `ProductId` varchar(128) AS (JSON_VALUE(json_data, '$.ProductId')) VIRTUAL,
    """

    insert_sql = f"""

    use {data["dbname"]}
    INSERT INTO {data["table_name"]} (json_data) VALUES (%s)
        """



    file = os.path.join(app.config["UPLOAD_FOLDER"], "upload.json")
    with open(file, 'r') as f:
        records = ujson.dumps(f.read())


    cur.executeMany(insert_sql,records)
    conn.commit()

    return render_template('json_to_sql/upload.html')
