from app.dao import chef as chef_dao
from app.controllers.admin import file as file_controller

def create_chef(form, file):
    chef_name = form.name.data
    chef_avatar = file['avatar']
    file_id = file_controller.create_file(chef_avatar)
    
    return chef_dao.create_chef(name=chef_name, file_id=file_id)

def show_chef(chef_id):
    chef = chef_dao.find_chef(chef_id)
    file = file_controller.find_file(chef.file_id)
    chef.avatar = file.name
    
    return chef

def edit_chef(chef_id, file, form):
    chef_name = form.name.data
    chef_avatar = file['avatar']
    
    if chef_avatar:
        print(chef_avatar)
        # update do arquivo
        #pass
    
    return chef_dao.update_chef(chef_id, chef_name)

    
