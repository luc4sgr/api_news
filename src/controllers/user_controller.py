from flask import request, jsonify
from src.services.user_service import UserService
from src.validators.user_validator import validate_create_user

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def create(self):
        data = validate_create_user(request)
        user = self.user_service.create_user(**data)
        return jsonify(user.to_dict()), 201

    def list(self):
        users_lits = self.user_service.list_users()
        return jsonify([user.to_dict() for user in users_lits]), 200
