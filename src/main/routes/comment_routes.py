from flask import Blueprint
from src.controllers.comment_controller import CommentController

comment_bp = Blueprint('comment', __name__, url_prefix='/comments')
controller = CommentController()

comment_bp.route("", methods=["POST"])(controller.create)
comment_bp.route("/<int:news_id>", methods=["GET"])(controller.list)
