from flask import request, Response
import os
from ui import app

def upload_file():
    if request.method == 'POST':
        file_ext = request.args.to_dict().get("file_ext")
        file = request.files['file']
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"upload.{file_ext}"))
    return Response("{'msg':'success'}", status=200, mimetype='application/json')