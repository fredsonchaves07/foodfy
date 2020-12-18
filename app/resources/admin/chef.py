from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin.form import RegistrationChef
from app.controllers.admin import chef as chef_controler

chefs = Blueprint('chefs', __name__, url_prefix='/admin/chefs')

@chefs.route('/', methods=['GET'])
def list_chefs():
    chefs = chef_controler.list_chefs()
    return render_template('admin/chef/index.html', chefs=chefs)


@chefs.route('/create', methods=['GET', 'POST'])
def create_chef():
    form = RegistrationChef(request.form)
    file = request.files
    
    if request.method == 'POST':
        chef_id = chef_controler.create_chef(form, file)

        return redirect(url_for('chefs.show_chef', chef_id=chef_id))
    return render_template('admin/chef/create.html', form=form)


@chefs.route('/<chef_id>', methods=['GET'])
def show_chef(chef_id):
    chef = chef_controler.show_chef(chef_id)
    
    return render_template('admin/chef/view.html', chef=chef)


@chefs.route('/<chef_id>/edit', methods=['GET', 'POST'])
def edit_chef(chef_id):
    chef = chef_controler.show_chef(chef_id)
    form = RegistrationChef(obj=chef)
    file = request.files
    
    if request.method == 'POST':
        if request.form['_method'] == 'PUT':
            chef_controler.edit_chef(chef_id, file, form)

            return redirect(url_for('chefs.show_chef', chef_id=chef_id))
        
        if request.form['_method'] == 'DELETE':
            chef_controler.delete_chef(chef_id)

            return redirect(url_for('chefs.create_chef'))
        

    return render_template('admin/chef/edit.html', chef=chef, form=form)

