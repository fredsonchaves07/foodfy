from app.db import db
from app.db.models import File

def create_file(filename, path):
    file = File(name=filename, path=path)
    db.session.add(file)
    db.session.commit()
    
    return file.id

def find_file(file_id):
    file = File.query.filter_by(id=file_id).first()

    return file

def update_file(filename, path, file_id):
    file = File.query.get(file_id)
    file.name = filename
    file.path = path
    db.session.add(file)
    db.session.commit()
    
    return