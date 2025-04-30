from sqlalchemy import Column, String, Integer
from src.database.config import Base

class NewsORM(Base):
    __tablename__ = "news"

    news_id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(String, nullable=False)
    category = Column(String, nullable=False)
    likes = Column(Integer, default=0)
