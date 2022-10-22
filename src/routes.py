from src import app
from .views.index import index
from utils.file_upload_utils import user_upload_file
from utils.get_data_from_database import get_data_from_database
from .views.csv_to_sql.csv_to_sql import csv_to_sql
from .views.json_to_sql.json_to_sql import json_to_sql, json_to_sql_upload
from .views.schema_form import schema_form

#views
app.add_url_rule('/', view_func=index)
app.add_url_rule('/csv-to-sql', view_func=csv_to_sql,
                    methods = ['POST', 'GET'])
app.add_url_rule('/json-to-sql', view_func=json_to_sql,
                    methods = ['POST', 'GET'])
app.add_url_rule('/schema', view_func=schema_form,
                    methods = ['POST', 'GET'])
#utility functions
app.add_url_rule('/user-upload-file', view_func=user_upload_file,
                 methods=['POST', 'GET'])
app.add_url_rule('/json-sql-upload', view_func=json_to_sql_upload,
                 methods=['POST', 'GET'])                                  

