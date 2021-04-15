from app.dao import user as user_dao


def login(user_fom):
    email = user_form['email']
    password = user_form['password']
    
    user = user_dao.login(email, password)
    
    return user
