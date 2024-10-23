from flask import Blueprint, request, jsonify
from app.models.user import User
from app.models.data_handler import data_handler

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return "Hello, Team!"


@main.route("/api/send_name", methods=['POST'])
def send_name():
    data = request.get_json()
    name = data.get('name')
    last_name = data.get('last_name')
    user = User(name, last_name)
    data_handler.add_user(user)
    return jsonify({
        "message": f"Name and last name received: {name} {last_name}"
    }), 200


@main.route("/api/get_greetings", methods=['GET'])
def get_greetings():
    greetings = [f"Hello {user.name} {user.last_name}" for user in data_handler.get_users()]
    return jsonify({
        "greetings": greetings
    }), 200


@main.route("/api/users", methods=['GET'])
def get_users():
    users = data_handler.get_users()
    users_list = [{"id": user.id, "name": user.name, "last_name": user.last_name} for user in users]
    return jsonify({
        "users":users_list
    }), 200


@main.route("/api/update_user/<user_id>", methods=['PUT', 'PATCH'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    last_name = data.get('last_name')
    user = data_handler.get_user(user_id)
    if user:
        if name:
            user.name = name
        if last_name:
            user.last_name = last_name
        return jsonify({
            "message":f"Updated user: {user.name} {user.last_name}"
        }), 200
    else:
        return jsonify({
            "message": "User not found"
        }), 404

@main.route("/api/delete_user/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    success = data_handler.delete_user(user_id)
    if success:
        return jsonify({
            "message":"Deleted user"
        }), 200
    else:
        return jsonify({
            "message":"User not found"
        }), 404