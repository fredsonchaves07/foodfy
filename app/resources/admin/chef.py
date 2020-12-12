from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin.form import RegistrationChef
from app.controllers.admin import chef as chef_controler

chefs = Blueprint('chefs', __name__, url_prefix='/admin/chefs')

@chefs.route('/create', methods=['GET', 'POST'])
def create_chef():
    form = RegistrationChef(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        chef_controler.create_chef(form)

        return redirect(url_for('list_chefs'))
    return render_template('admin/chef/create.html', form=form)
