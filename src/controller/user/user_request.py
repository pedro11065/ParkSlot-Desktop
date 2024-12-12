from flask import Blueprint, request, render_template

auth_user = Blueprint('auth_user', __name__, template_folder='templates', static_folder='static')

@auth_user.route('/register') #methods=['GET', 'POST']
def register():
    return render_template('user/register.html')

@auth_user.route('/login') #methods=['GET', 'POST']
def login():
    return render_template('user/login.html')
