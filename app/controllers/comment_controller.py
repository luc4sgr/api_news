from flask import Blueprint, request, jsonify
from app.services.comment_service import CommentService

comment_bp = Blueprint('comment', __name__, url_prefix='/comments')
comment_service = CommentService()

@comment_bp.route("", methods=['POST'])
def create_comment():
    data = request.get_json()
    content = data.get('content')
    news_id = data.get("news_id")
    user_id = data.get("user_id")
    comment  = comment_service.create_comment(
        content=content,
        news_id=news_id,
        user_id=user_id,
        )
    
    return jsonify({
        'comment_id' : comment.comment_id,
        'news_id' : comment.news_id,
        'user_id' : comment.user_id,
        'content' : comment.content,
        }), 201

@comment_bp.route('/<int:news_id>', methods=['GET'])
def list_comments(news_id):
    comments = comment_service.list_comments(news_id=news_id)
    result = [{
        'comment_id' : comment.comment_id,
        'news_id' : comment.news_id,
        'user_id' : comment.user_id,
        'content' : comment.content,
        } for comment in comments]
    return jsonify(result), 200