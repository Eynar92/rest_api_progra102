from flask import Flask
from dotenv import load_dotenv
import os

from app.routes.main import main
from app.routes.users import user_routes
from app.routes.files import files_routes
from app.routes.auth import auth_routes


def create_app():
    app = Flask(__name__)

    # Load enviroment variables from .env
    load_dotenv()

    # Aditional config
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = 'app/uploads'

    # Blueprint register
    app.register_blueprint(main)
    app.register_blueprint(user_routes)
    app.register_blueprint(files_routes)
    app.register_blueprint(auth_routes)

    return app
