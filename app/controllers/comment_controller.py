from flask import Blueprint, request, jsonify
from app.services.comment_service import CommentService
from app.validators.comment_validator import validate_create_comment

comment_bp = Blueprint('comment', __name__, url_prefix='/comments')
comment_service = CommentService()

@comment_bp.route("", methods=['POST'])
def create_comment():
    data = validate_create_comment(request)
    comment = comment_service.create_comment(**data)

    return jsonify(comment.to_dict()), 201

@comment_bp.route('/<int:news_id>', methods=['GET'])
def comments_list(news_id):
    comments_list = comment_service.comments_list(news_id=news_id)
    result = [comment.to_dict() for comment in comments_list]
    return jsonify(result), 200