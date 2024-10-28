import os
from flask import Blueprint, request, jsonify

files_routes = Blueprint('files', __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@files_routes.route("/api/files/upload", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({
            "success": False,
            "message": 'No file part'
        }), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({
            "success": False,
            "message": "No selected file"
        }), 400
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        url = f"/uploads/{filename}"
        return jsonify({
            "success": True,
            "message": "File successfully uploaded",
            "url": url
        }), 200
    return jsonify({
        "success": False,
        "message": "File type not allowed"
    }), 400
