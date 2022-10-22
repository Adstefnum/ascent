
from flask_wtf import FlaskForm
from wtforms import StringField

class SchemaForm(FlaskForm):
    dummy = StringField('dummy')