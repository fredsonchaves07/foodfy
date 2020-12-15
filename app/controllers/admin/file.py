import os
from flask import current_app
from werkzeug.utils import secure_filename
from datetime import datetime
from app.dao import file as file_dao

def create_file(file):
    now = datetime.utcnow()
    filename = secure_filename(os.path.join(str(now), file.filename))
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    return file_dao.create_file(filename, path)

    