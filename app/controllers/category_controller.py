from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService

category_bp = Blueprint('category', __name__, url_prefix='/categories')
catagory_service = CategoryService()

@category_bp.route("", methods=['POST'])
def create_catagory():
    data = request.get_json()
    name = data.get("name")
    catagory  = catagory_service.create_category(name=name)
    
    return jsonify({'name':catagory.name}), 201

@category_bp.route('', methods=['GET'])
def list_catagory():
    catagories = catagory_service.list_catagorys()
    result = [{'name':catagory.name} for catagory in catagories]
    return jsonify(result), 200