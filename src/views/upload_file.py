from flask import request, url_for, redirect, render_template
import os
from src import app


def user_upload_file(file_ext, endpoint):
    if request.method == 'POST': 
        uploaded_file = request.files['file']
        if uploaded_file:
            uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"upload.{file_ext}"))
        else:
            return redirect(url_for('error_view',message="You didn't upload a file"))
    return render_template("upload_file.html",endpoint=endpoint)

    
    