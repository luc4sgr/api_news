from flask import Blueprint
from src.controllers.user_controller import UserController

user_bp = Blueprint("user", __name__, url_prefix="/users")
controller = UserController()

user_bp.route("", methods=["POST"])(controller.create)
user_bp.route("", methods=["GET"])(controller.list)
