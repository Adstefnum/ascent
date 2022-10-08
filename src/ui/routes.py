from ui import app
from .views.index import index
from utils.upload_file import upload_file
from utils.get_data_from_database import get_data_from_database
from .views.csv_to_database.csv_to_database import csv_to_database

app.add_url_rule('/', view_func=index)
app.add_url_rule('/upload-file', view_func=upload_file,
                 methods=['POST', 'GET'])
app.add_url_rule('/csv-to-database', view_func=csv_to_database,
                    methods = ['POST', 'GET'])



