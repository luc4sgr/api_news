from src.repositories.base.news_repository import NewsRepository
from src.database.models.news_orm import NewsORM
from src.database.config import SessionLocal

class PostgresNewsRepository(NewsRepository):
    def __init__(self):
        self.db = SessionLocal()

    def create(self, news):
        news_orm = NewsORM(
            news_id=news.news_id,
            title=news.title,
            content=news.content,
            author_id=news.author_id,
            category=news.category,
            likes=news.likes
        )
        self.db.add(news_orm)
        self.db.commit()

    def list(self):
        return self.db.query(NewsORM).all()

    def like(self, news_id):
        news = self.db.query(NewsORM).filter(NewsORM.news_id == news_id).first()
        if news:
            news.likes += 1
            self.db.commit()
        return news
