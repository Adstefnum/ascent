from flask import render_template

def json_to_database():
    return render_template('csv_to_database/index.html',file_ext="json")