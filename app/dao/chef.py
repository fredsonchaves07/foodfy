from datetime import datetime
from app.db import db
from app.db.models import File, Chef

def create_chef(name, file_id, ):
    chef = Chef(name=name, file_id=file_id)
    db.session.add(chef)
    db.session.commit()
    
    return chef.id

def find_chef(chef_id):
    chef = Chef.query.filter_by(id=chef_id).first()
    
    return chef

def update_chef(chef_id, chef_name):
    chef = Chef.query.get(chef_id)

    if chef_name != chef.name:
        chef.name = chef_name
        chef.modified_at = datetime.utcnow()
        db.session.add(chef)
        db.session.commit()   
    
    return 

def delete_chef(chef):
    db.session.delete(chef)
    db.session.commit()
    
    return
