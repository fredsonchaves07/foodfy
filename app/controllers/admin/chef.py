from app.dao import chef as chef_dao
from app.controllers.admin import file as file_controller

def create_chef(form, file):
    chef_name = form.name.data
    file_id = file_controller.create_file(file['avatar'])
    
    # Registrar o chef

