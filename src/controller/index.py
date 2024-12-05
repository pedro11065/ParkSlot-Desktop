from flask import Blueprint, request, render_template

index = Blueprint('auth_index', __name__, template_folder='templates', static_folder='static')

@index.route('/') #methods=['GET', 'POST']
def home():
    return render_template('index.html')
