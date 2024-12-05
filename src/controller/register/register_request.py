from flask import Blueprint, request, render_template
from flask_login import login_required
from src.controller.register.entry.register_entry import entry

#tudo aqui é: /company...

register_request = Blueprint('auth_register', __name__, template_folder='templates', static_folder='static')

@register_request.route('/entry', methods= ['POST','GET']) #methods=['GET', 'POST']
def register_entry():
    if request.method == 'POST':
        data = request.get_json()
        return entry(data)
    else:
        return render_template('register/entry.html')
