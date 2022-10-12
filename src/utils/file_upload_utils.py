from flask import request, Response
import os
from src import app
import ujson
import pandas
import logging
import shortuuid
import pprint
from .dbutils import get_connection

def user_upload_file(file_ext):
    if request.method == 'POST': 
        file = request.files['file']
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"upload.{file_ext}"))
    return Response("{'msg':'success'}", status=200, mimetype='application/json')

def csv_to_sql_upload():
    
    df = pd.read_csv(f"{filename}.csv", encoding='utf-8-sig')  #    latin1
  
    sql = """INSERT INTO inv_upload_g (bgr_exclude_bra365,bgr_invoice_this_line, json_data)
             VALUES (%s, %s, %s)"""
    
    data = df.fillna('').to_dict(orient="records")
    cursor = get_connection().cursor()
    for item in data:
        item['id'] = shortuuid.uuid()
        logging.debug(f'\n' + pprint.pformat(item, indent=2, sort_dicts=False))
        json_data = ujson.dumps(item)


        #TODO: use transactions
        sql_update(sql, (exclude_bra_365,inv_this_line, json_data),cursor=cursor, autocommit=True)

    return Response("{'msg':'success'}", status=200, mimetype='application/json')

def flush_uploads_folder():
    #  os.system(f"rm -rf {app.config["UPLOAD_FOLDER"]}/*")
    pass
    
    