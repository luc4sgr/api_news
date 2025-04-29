from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.validators.user_validator import validate_create_user

user_bp = Blueprint('user', __name__, url_prefix='/users')
user_service = UserService()

@user_bp.route("", methods=['POST'])
def create_user():
    data = validate_create_user(request)
    user = user_service.create_user(**data)
    
    return jsonify({
        "user_id": user.user_id,
        "username": user.username
    }), 201


@user_bp.route('', methods=['GET'])
def list_users():
    list_users = user_service.list_users()
    result = [{'user_id':user.user_id, 'username':user.username} for user in list_users]
    return jsonify(result), 200