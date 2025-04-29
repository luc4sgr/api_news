from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService
from app.validators.category_validator import validate_create_category

category_bp = Blueprint('category', __name__, url_prefix='/categories')
catagory_service = CategoryService()

@category_bp.route("", methods=['POST'])
def create_catagory():
    data = validate_create_category(request)
    catagory  = catagory_service.create_category(**data)
    
    return jsonify(catagory.to_dict()), 201

@category_bp.route('', methods=['GET'])
def categories_list():
    categories_list = catagory_service.list_catagorys()
    result = [catagory.to_dict() for catagory in categories_list]
    return jsonify(result), 200