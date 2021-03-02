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

def find_file(file_id):
    file = file_dao.find_file(file_id)

    return file

def update_file(new_file, old_file):
    now = datetime.utcnow()
    filename = secure_filename(os.path.join(str(now), new_file.filename))
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    os.remove(old_file.path)
    new_file.save(path)
    
    return file_dao.update_file(filename, path, old_file.id)

def remove_file(file):
    # os.remove(file.path)
    file_dao.remove_file(file)
    
    