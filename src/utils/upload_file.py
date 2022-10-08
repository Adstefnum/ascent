def upload_file(file_ext):
    if request.method == 'POST':
        file = request.files['file']
        file.save(f"../../uploads/upload.{file_ext}")
    return 200