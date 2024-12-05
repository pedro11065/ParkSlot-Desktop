from src import create_app
from flask_cors import CORS

app = create_app();
CORS(app) 
app.app_context().push()
if __name__ == '__main__': 
    app.run(debug=True);    
