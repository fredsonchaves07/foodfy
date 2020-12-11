from flask import Blueprint, redirect, url_for

site = Blueprint('site', __name__, url_prefix='/')

@site.route('/', methods=['GET'])
def index():
    return redirect(url_for('admin.index'))
