from flask import Blueprint, request, render_template, redirect, url_for
from app.controllers.site import chef as chef_controller


site = Blueprint('site', __name__, url_prefix='/')


@site.route('/about', methods=['GET'])
def index():
    return render_template('site/about.html')