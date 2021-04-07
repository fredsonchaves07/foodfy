from flask import Blueprint, request, render_template, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def login():
    return 'oi'