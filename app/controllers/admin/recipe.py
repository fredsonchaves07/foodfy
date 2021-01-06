from app.dao import chef as chef_dao

def list_chef_recipe():
    chefs = chef_dao.all_chef() 

    return [(chef[0], chef[2]) for chef in chefs]
