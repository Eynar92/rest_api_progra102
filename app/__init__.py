from flask import Flask
from app.routes.main import main
from app.routes.users import user_routes
from app.routes.files import files_routes
from app.routes.auth import auth_routes


def create_app():
    app = Flask(__name__)

    # Blueprint register
    app.register_blueprint(main)
    app.register_blueprint(user_routes)
    app.register_blueprint(files_routes)
    app.register_blueprint(auth_routes)

    # Aditional config
    app.config['UPLOAD_FOLDER'] = 'app/uploads'
    app.config['SECRET_KEY'] = 'secretkey123..,'

    return app
