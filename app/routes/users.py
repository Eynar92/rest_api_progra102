from flask import Blueprint, request, jsonify
from app.models.data_handler import data_handler
from app.utils.auth import token_required

user_routes = Blueprint('users', __name__)


@user_routes.route("/api/users", methods=['GET'])
@token_required
def get_users():
    users = data_handler.get_users()
    users_list = [
        {
            "id": user.id,
            "name": user.name,
            "last_name": user.last_name,
        } for user in users]
    return jsonify({
        "success": True,
        "users": users_list
    }), 200


@user_routes.route("/api/users/<user_id>", methods=['GET'])
@token_required
def get_user(user_id):
    user = data_handler.get_user(user_id)
    if user:
        return jsonify({
            "success": True,
            "user": {
                "id": user.id,
                "name": user.name,
                "last_name": user.last_name
            }
        }), 200


@user_routes.route("/api/users/<user_id>", methods=['PUT', 'PATCH'])
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
            "success": True,
            "message": "Successfully updated user data"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 400


@user_routes.route("/api/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    success = data_handler.delete_user(user_id)
    if success:
        return jsonify({
            "success": True,
            "message": "Deleted user"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404
