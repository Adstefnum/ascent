from src.ui.app import app
from src.ui.app import index
from src.utils.upload_file import upload_file
from src.utils.get_data_from_database import get_data_from_database

app.add_url_rule('/', view_func=index)
app.add_url_rule('/upload-file', view_func=upload_file,
                 methods=['POST', 'GET'])



