from src.repositories.base.comment_repository import CommentRepository
from src.database.models.comment_orm import CommentORM
from src.database.config import SessionLocal

class PostgresCommentRepository(CommentRepository):
    def __init__(self):
        self.db = SessionLocal()

    def create(self, comment):
        comment_orm = CommentORM(
            comment_id=comment.comment_id,
            content=comment.content,
            news_id=comment.news_id,
            user_id=comment.user_id
        )
        self.db.add(comment_orm)
        self.db.commit()

    def list_by_news(self, news_id):
        return self.db.query(CommentORM).filter_by(news_id=news_id).all()
