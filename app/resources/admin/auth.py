from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.admin import auth as auth_controller

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        user = auth_controller.login(request.form)
        
        if user:
            return redirect(url_for('recipes.list_recipes'))
        
    
    return render_template('admin/login.html')
