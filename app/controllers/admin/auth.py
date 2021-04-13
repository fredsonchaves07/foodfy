from app.dao import auth as auth_dao


def login(user_fom):
    email = user_form['email']
    password = user_form['password']
    
    user = auth_dao.login(email, password)
    
    return user
