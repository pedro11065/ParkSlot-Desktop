from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='view/static', template_folder='view/templates')
    app.config['SECRET_KEY'] = 'chave_secreta_nome' #Responsável por encriptar os cookies e session data (Ainda não utilizado).

    from .controller.parking.register.register_request import register_request 
    from .controller.index import index

    app.register_blueprint(register_request, url_prefix='/register')
    app.register_blueprint(index, url_prefix='/')
    
    return app;