import jwt
from functools import wraps
from flask import request, jsonify, current_app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({
                "success": False,
                "message": "Token is missing"
            }), 401

        try:
            data = jwt.decode(
                token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({
                "success": False,
                "message": "Token is invalid"
            }), 401
        return f(*args, **kwargs)
    return decorated
