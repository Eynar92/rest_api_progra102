import jwt
import datetime
from flask import Blueprint, request, jsonify, current_app
from app.models.user import User
from app.models.data_handler import data_handler

auth_routes = Blueprint('auth', __name__)


@auth_routes.route("/api/auth/register", methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    last_name = data.get('last_name')
    password = data.get('password')
    user = User(name, last_name, password)
    data_handler.add_user(user)
    return jsonify({
        "success": True,
        "message": "User registered successfully"
    }), 201


@auth_routes.route("/api/auth/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = data_handler.authenticate(username, password)
    if user:
        token = jwt.encode(
            {
                'id': user.id,
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )

        return jsonify({
            "success": True,
            "message": "Login successfully",
            "token": token
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Invalid credentials"
        }), 401
