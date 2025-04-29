from flask import request, jsonify
from src.services.category_service import CategoryService
from src.validators.category_validator import validate_create_category

class CategoryController:
    def __init__(self):
        self.category_service = CategoryService()

    def create(self):
        data = validate_create_category(request)
        category = self.category_service.create_category(**data)
        return jsonify(category.to_dict()), 201

    def list(self):
        categories = self.category_service.list_categories()
        return jsonify([category.to_dict() for category in categories]), 200
