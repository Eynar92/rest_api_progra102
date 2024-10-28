from flask import Blueprint, request, jsonify
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
        return jsonify({
            "success": True,
            "message": "Login successfully",
            "user": {
                "id": user.id,
                "name": user.name,
                "last_name": user.last_name
            }
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Invalid credentials"
        }), 401
