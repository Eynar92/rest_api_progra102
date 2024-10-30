import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.models.gender_recognizer import GenderRecognizer

gender_recognizer_routes = Blueprint('gender_recognizer', __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@gender_recognizer_routes.route('/api/gender_recognizer/', methods=['POST'])
def gender_recognizer():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Rest of params
        accuracy = request.get('accuracy')
        model = request.get('model')
        gender = request.get('gender')

        # Class instance and call method recognize
        recognizer = GenderRecognizer(model)
        result = recognizer.recognize(file_path, accuracy)

        return jsonify({"success": True, "message": "Gender recognition completed", "result": result}), 200
    return jsonify({"success": False, "message": "File type not allowed"}), 400
