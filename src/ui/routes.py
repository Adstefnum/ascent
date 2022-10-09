from ui import app
from .views.index import index
from utils.file_upload_utils import user_upload_file, csv_to_database_upload, json_to_database_upload
from utils.get_data_from_database import get_data_from_database
from .views.csv_to_database.csv_to_database import csv_to_database
from .views.json_to_database.json_to_database import json_to_database

#views
app.add_url_rule('/', view_func=index)
app.add_url_rule('/csv-to-database', view_func=csv_to_database,
                    methods = ['POST', 'GET'])
app.add_url_rule('/json-to-database', view_func=json_to_database,
                    methods = ['POST', 'GET'])

#utility functions
app.add_url_rule('/user-upload-file', view_func=user_upload_file,
                 methods=['POST', 'GET'])
app.add_url_rule('/csv-database-upload', view_func=csv_to_database_upload,
                 methods=['POST', 'GET'])
app.add_url_rule('/json-database-upload', view_func=json_to_database_upload,
                 methods=['POST', 'GET'])                                  

