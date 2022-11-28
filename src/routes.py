from src import app
from .views.index import index
from .views.upload_file import user_upload_file
from .views.json_to_sql.json_to_sql import json_to_sql, json_to_sql_upload
from .views.schema_form import schema_form_get, schema_form_post
from .views.error_pages import error_view

#views
app.add_url_rule('/', view_func=index)
app.add_url_rule('/messages/<message>', view_func=error_view)
app.add_url_rule('/json-to-sql', view_func=json_to_sql,
                    methods = ['POST','GET'])
app.add_url_rule('/schema-get/<conn_data>', view_func=schema_form_get,
                    methods = ['GET'])
app.add_url_rule('/schema-post/', view_func=schema_form_post,
                    methods = ['POST'])
#utility functions
app.add_url_rule('/user-upload-file/<file_ext>/<endpoint>/', view_func=user_upload_file,
                 methods=['POST','GET'])
app.add_url_rule('/json-sql-upload', view_func=json_to_sql_upload,
                 methods=['POST', 'GET'])

