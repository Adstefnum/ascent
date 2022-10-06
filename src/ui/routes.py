from ui import app
from ui.app import index
from utils.upload_file import upload_file
from utils.get_data_from_database import get_data_from_database

app.add_url_rule('/', view_func=index)
app.add_url_rule('/upload-file', view_func=upload_file,
                 methods=['POST', 'GET'])



