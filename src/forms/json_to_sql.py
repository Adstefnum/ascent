from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField,BooleanField,IntegerField,TextAreaField,validators
from .jsonfield import JsonField
from .custom_validators import RequiredIf, OptionalIfFieldEqualTo

def validate_host(form,field):
    return validators.URL(field) or validators.IPAddress(field)

class JsonToDatabaseForm(FlaskForm):

   #TODO file upload is not yet compulsory, people might forget , maybe add it to form and validate it then save it with upload file
   #you can add hidden to it so it is not displayed in the loop or just exclude it from the loop another way and then display it on your own
   #use the actual name of the file to allow multiple users connect at once?
    # recaptcha = RecaptchaField()
    use_tcp = BooleanField('Use tcp?',default="checked")
    unix_socket = StringField('Unix Socket',[OptionalIfFieldEqualTo('use_tcp','y')])
    # host = StringField('Host',[validators.Regexp(regex=r"(?!w)(\w+\.\w+\.\w+|^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3} (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$)")])
    host = StringField('Host',[validate_host, RequiredIf('use_tcp')])
    port = IntegerField('Port',[validators.DataRequired(),validators.NumberRange(min=0,max=65537)])
    user = StringField('User',[validators.InputRequired()])
    dbname =  StringField('Database Name',[validators.InputRequired()])
    dbpass = PasswordField('Password',[validators.InputRequired()])
    table_name = StringField('Table Name',[validators.InputRequired()])
    create_table = BooleanField('Create table?',default="")
    col_to_json_key_map = JsonField('Column name to JSON key maps')
    schema = TextAreaField('Sql Schema',[OptionalIfFieldEqualTo('use_tcp','y')])

# TODO validation needs more work, people can also fill both unix and host if they choose, fixz this
# TODO add placeholder for confusing fields like col_to_json, later add more visual option
