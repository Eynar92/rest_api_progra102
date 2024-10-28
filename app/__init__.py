from flask import Flask
from app.routes.main import main
from app.routes.users import user_routes


def create_app():
    app = Flask(__name__)

    # Blueprint register
    app.register_blueprint(main)
    app.register_blueprint(user_routes)

    # Aditional config
    app.config['UPLOAD_FOLDER'] = 'app/uploads'
    
    return app
