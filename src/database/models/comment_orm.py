from sqlalchemy import Column, String, ForeignKey
from src.database.config import Base

class CommentORM(Base):
    __tablename__ = "comments"

    comment_id = Column(String, primary_key=True)
    content = Column(String, nullable=False)
    news_id = Column(String, ForeignKey("news.news_id"), nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
