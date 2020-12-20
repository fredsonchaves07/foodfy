from flask import Blueprint, redirect, url_for

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/', methods=['GET'])
def index():
    return redirect(url_for('chefs.create_chef'))
