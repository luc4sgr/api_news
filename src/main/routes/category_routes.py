from flask import Blueprint
from src.controllers.category_controller import CategoryController

category_bp = Blueprint("category", __name__, url_prefix="/categories")
controller = CategoryController()

category_bp.route("", methods=["POST"])(controller.create)
category_bp.route("", methods=["GET"])(controller.list)
