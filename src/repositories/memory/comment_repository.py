from src.repositories.base.comment_repository import CommentRepository
from src.models.comment import Comment

class InMemoryCommentRepository(CommentRepository):
    def __init__(self):
        self.comments: list[Comment] = []

    def create(self, comment: Comment):
        self.comments.append(comment)

    def list_by_news(self, news_id: str) -> list[Comment]:
        return [c for c in self.comments if c.news_id == news_id]
