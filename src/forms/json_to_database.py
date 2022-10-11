from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField,BooleanField
from jsonfield import JsonField

class JsonToDatabaseForm(FlaskForm):
    recaptcha = RecaptchaField()
    use_tcp = BooleanField('use_tcp',[validators.required])
    unix_socket = StringField('unix_socket')
    host = StringField('host',[validators.required])
    user = StringField('user',[validators.required])
    dbname =  StringField('database_name',[validators.required])
    dbpass = PasswordField('passowrd',[validators.required])
    table_name = StringField('table_name',[validators.required])
    table_created = BooleanField('table_created',[validators.required])
    col_to_json_key_map = JsonField('maps',[validators.required])
