from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService
from app.validators.category_validator import validate_create_category

category_bp = Blueprint('category', __name__, url_prefix='/categories')
catagory_service = CategoryService()

@category_bp.route("", methods=['POST'])
def create_catagory():
    data = validate_create_category(request)
    catagory  = catagory_service.create_category(**data)
    
    return jsonify({'name':catagory.name}), 201

@category_bp.route('', methods=['GET'])
def list_category():
    list_category = catagory_service.list_catagorys()
    result = [{'name':catagory.name} for catagory in list_category]
    return jsonify(result), 200