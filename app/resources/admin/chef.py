from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin.form import RegistrationChef
from app.controllers.admin import chef as chef_controler

chefs = Blueprint('chefs', __name__, url_prefix='/admin/chefs')

@chefs.route('/create', methods=['GET', 'POST'])
def create_chef():
    form = RegistrationChef(request.form)
    file = request.files
    
    if request.method == 'POST':
        chef_controler.create_chef(form, file)

        # return redirect(url_for('create_chef'))
    return render_template('admin/chef/create.html', form=form)
