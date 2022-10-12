from flask import render_template

def csv_to_sql():
    return render_template('csv_to_sql/index.html',file_ext="csv")