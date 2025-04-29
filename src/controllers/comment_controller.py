from flask import request, jsonify
from src.services.comment_service import CommentService
from src.validators.comment_validator import validate_create_comment

class CommentController:
    def __init__(self):
        self.comment_service = CommentService()

    def create(self):
        data = validate_create_comment(request)
        comment = self.comment_service.create_comment(**data)
        return jsonify(comment.to_dict()), 201

    def list(self, news_id):
        comments = self.comment_service.list_comments(news_id=news_id)
        return jsonify([comment.to_dict() for comment in comments]), 200
