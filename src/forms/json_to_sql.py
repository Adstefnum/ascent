from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField,BooleanField,IntegerField,TextAreaField
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
    create_table = BooleanField('Create table?',default="unchecked")
    col_to_json_key_map = JsonField('Column name to JSON key maps')
    schema = TextAreaField('Sql Schema')

#next step is to make the default of create_table unchecked
#validation is the next step
