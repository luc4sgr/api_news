from src.repositories.base.news_repository import NewsRepository
from src.models.news import News

class InMemoryNewsRepository(NewsRepository):
    def __init__(self):
        self.news: list[News] = []

    def create(self, news: News):
        self.news.append(news)

    def list(self) -> list[News]:
        return self.news

    def like(self, news_id: str) -> News | None:
        for news in self.news:
            if news.news_id == news_id:
                news.likes += 1
                return news
        return None
