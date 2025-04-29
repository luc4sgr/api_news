from flask import Blueprint
from src.controllers.news_controller import NewsController

news_bp = Blueprint("news", __name__, url_prefix="/news")
controller = NewsController()

news_bp.route("", methods=["POST"])(controller.create)
news_bp.route("", methods=["GET"])(controller.list)
news_bp.route("/<int:news_id>/like", methods=["POST"])(controller.like)
