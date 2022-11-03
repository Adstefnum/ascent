
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SelectField, SelectMultipleField,FormField, FieldList

class SchemaField(Form):
    json_key = StringField('JSON Key')
    col_name = StringField('Column Name')
    data_type = SelectField('Data Type', choices=[
    ("varchar","VARCHAR"),
    ("text","TEXT"),
    ("int","INT"),
    ("float","FLOAT"),
    ("boolean","BOOLEAN"),
    ("date","DATE"),
    ("datetime","DATETIME"),
    ("timestamp","TIMESTAMP"),
    ])
    constraint = SelectMultipleField('Constraint',choices=[
            ("unique","UNIQUE"),
    ("primary key","PRIMARY KEY"),
    ("foreign key","FOREIGN KEY"),
    ("auto_increment","AUTO INCREMENT"),
    ("not_null","NOT NULL"),
    ])

class SchemaForm(Form):
    schema = FieldList(FormField(SchemaField),min_entries=1)
