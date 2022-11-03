from flask_wtf import FlaskForm, RecaptchaField,Form
from wtforms import StringField, PasswordField,BooleanField,IntegerField\
,TextAreaField,validators,SelectField, FieldList, FormField,SelectMultipleField\
,FileField
from .jsonfield import JsonField
from .custom_validators import RequiredIf, OptionalIfFieldEqualTo

def validate_host(form,field):
    return validators.URL(field) or validators.IPAddress(field)


class JsonToDatabaseForm(FlaskForm):

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
    table_exists = BooleanField('Table Exists?',default="checked")

# TODO validation needs more work, people can also fill both unix and host if they choose, fixz this
