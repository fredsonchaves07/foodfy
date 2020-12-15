from app.dao import chef as chef_dao
from app.controllers.admin import file as file_controller

def create_chef(form, file):
    chef_name = form.name.data
    chef_avatar = file['avatar']
    file_id = file_controller.create_file(chef_avatar)
    
    return chef_dao.create_chef(name=chef_name, file_id=file_id)
    
