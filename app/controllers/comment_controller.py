from flask import Blueprint, request, jsonify
from app.services.comment_service import CommentService
from app.validators.comment_validator import validate_create_comment

comment_bp = Blueprint('comment', __name__, url_prefix='/comments')
comment_service = CommentService()

@comment_bp.route("", methods=['POST'])
def create_comment():
    data = validate_create_comment(request)
    comment = comment_service.create_comment(**data)

    return jsonify({
        "comment_id": comment.comment_id,
        "news_id": comment.news_id,
        "user_id": comment.user_id,
        "content": comment.content
    }), 201

@comment_bp.route('/<int:news_id>', methods=['GET'])
def list_comments(news_id):
    list_comments = comment_service.list_comments(news_id=news_id)
    result = [{
        'comment_id' : comment.comment_id,
        'news_id' : comment.news_id,
        'user_id' : comment.user_id,
        'content' : comment.content,
        } for comment in list_comments]
    return jsonify(result), 200