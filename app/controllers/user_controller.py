from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.validators.user_validator import validate_create_user

user_bp = Blueprint('user', __name__, url_prefix='/users')
user_service = UserService()

@user_bp.route("", methods=['POST'])
def create_user():
    data = validate_create_user(request)
    user = user_service.create_user(**data)
    
    return jsonify(user.to_dict()), 201


@user_bp.route('', methods=['GET'])
def users_list():
    users_list = user_service.users_list()
    result = [user.to_dict() for user in users_list]
    return jsonify(result), 200