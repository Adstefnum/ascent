from flask import render_template,request,Response
from forms.json_to_sql import JsonToDatabaseForm
from utils.dbutils import get_connection
from utils.file_upload_utils import user_upload_file

def json_to_sql():
    
    if request.method=="GET":
        form = JsonToDatabaseForm()
        return render_template('json_to_sql/index.html',file_ext="json",form=form)
    if request.method =="POST" and form.validate():
        data = form.to_dict()
        user_upload_file("json")
        return json_to_sql_upload(data)
        #I have to show like a status and progress bar while it is uploading, connecting to db, uploading to db and finished, then I redirect to homepage
    return Response("{'msg':'failure'}", status=404, mimetype='application/json')


def json_to_sql_upload(data ):
    
    conn = get_connection(data)
    cur = conn.cursor()

    transactions = []

    create_table_sql = """
    """

    insert_sql = """
         
        """ 



    file = os.path.join(app.config["UPLOAD_FOLDER"], "upload.json")
    
    with open(file, 'r') as f:
        data = ujson.loads(f.read())




    return Response("{'msg':'success'}", status=200, mimetype='application/json')
