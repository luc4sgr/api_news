from sqlalchemy import Column, String, ForeignKey, DateTime
from src.database.config import Base
from datetime import datetime

class LikeORM(Base):
    __tablename__ = "likes"

    user_id = Column(String, ForeignKey("users.user_id"), primary_key=True)
    news_id = Column(String, ForeignKey("news.news_id"), primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
