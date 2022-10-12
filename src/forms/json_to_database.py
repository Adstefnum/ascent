from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField,BooleanField,IntegerField
from .jsonfield import JsonField


class JsonToDatabaseForm(FlaskForm):
    # recaptcha = RecaptchaField()
    use_tcp = BooleanField('Use tcp?',default="checked")
    unix_socket = StringField('Unix Socket')
    host = StringField('Host')
    port = IntegerField('Port')
    user = StringField('User')
    dbname =  StringField('Database Name')
    dbpass = PasswordField('Password')
    table_name = StringField('Table Name')
    create_table = BooleanField('Create table?')
    col_to_json_key_map = JsonField('Column name to JSON key maps')
