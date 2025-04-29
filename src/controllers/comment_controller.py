from flask import request, jsonify
from src.services.comment_service import CommentService
from src.validators.comment_validator import validate_create_comment
from src.utils.paginator import paginate

class CommentController:
    def __init__(self):
        self.comment_service = CommentService()

    def create(self):
        data = validate_create_comment(request)
        comment = self.comment_service.create_comment(**data)
        return jsonify(comment.to_dict()), 201

    def list(self, news_id: str):
        params = request.args.to_dict(flat=True)
        comments = self.comment_service.list_comments(news_id=news_id)

        page = int(params.get("page", 1))
        per_page = int(params.get("per_page", 10))

        paginated = paginate([c.to_dict() for c in comments], page, per_page)
        return jsonify(paginated), 200
