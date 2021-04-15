from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin.form import RegistrationUser
from app.controllers.admin import user as user_controller

user = Blueprint('user', __name__, url_prefix='/admin/user')

@user.route('/create', methods=['GET', 'POST'])
def create_user():
    form = RegistrationUser(request.form)
    
    if request.method == 'POST':
        user_controller.create_user(form)
    
    return render_template('admin/user/create.html', form=form)
    