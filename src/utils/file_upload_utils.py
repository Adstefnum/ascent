from flask import request, Response
import os
from ui import app
import ujson
import pandas
import logging
import shortuuid
import pprint

def user_upload_file():
    if request.method == 'POST':
        file_ext = request.args.to_dict().get("file_ext")
        file = request.files['file']
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"upload.{file_ext}"))
    return Response("{'msg':'success'}", status=200, mimetype='application/json')

def json_to_database_upload():

    c = conn.cursor()

    sql = """
        INSERT INTO questions_api_question ( 
        question, option_A, option_B, option_C, option_D , option_E ,
        correct_ans , explain , subject, year, acom_type , exam_type , accompany_id 
        ) 
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"""


    def _valid(field):
    
        return field if not KeyError and field else None



        file = os.path.join(app.config["UPLOAD_FOLDER"], "upload.json")
        
        with open(file, 'r') as f:
            data = ujson.loads(f.read())

            for i in range(len(data)-1):
                question = data[i]['question']
                values = [
question , option_A , option_B , option_C , option_D , option_E , 
correct_ans , explain , subject, year, acom_type, exam_type, accompany_id

]

        c.execute(sql,values)

    conn.commit()
    conn.close()
    return Response("{'msg':'success'}", status=200, mimetype='application/json')

def csv_to_database_upload():
    
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
     os.system(f"rm -rf {app.config["UPLOAD_FOLDER"]}/*")
    
    