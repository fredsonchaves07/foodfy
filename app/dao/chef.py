from app.db import db
from app.db.models import File, Chef

def create_chef(name, file_id, ):
    chef = Chef(name=name, file_id=file_id)
    db.session.add(chef)
    db.session.commit()
    
    return chef.id