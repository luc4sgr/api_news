from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__, url_prefix='/users')
user_service = UserService()

@user_bp.route("", methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    user  = user_service.create_user(username)
    
    return jsonify({'user_id': user.user_id, 'username': user.username}), 201


@user_bp.route('', methods=['GET'])
def list_users():
    users = user_service.list_users()
    result = [{'user_id':user.user_id, 'username':user.username} for user in users]
    return jsonify(result), 200