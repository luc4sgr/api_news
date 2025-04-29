import uuid
from src.models.news import News
from src.repositories.memory.news_repository import InMemoryNewsRepository

class NewsService:
    def __init__(self):
        self.repo = InMemoryNewsRepository()

    def create_news(self, author_id: str, category: str, content: str, title: str = "") -> News:
        news_id = str(uuid.uuid4())
        news = News(news_id=news_id, author_id=author_id, category=category, content=content, title=title, likes=0)
        self.repo.create(news)
        return news

    def list_news(self) -> list[News]:
        return self.repo.list()

    def like_news(self, news_id: str) -> News | None:
        return self.repo.like(news_id)
