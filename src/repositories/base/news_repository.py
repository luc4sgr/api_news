from abc import ABC, abstractmethod
from src.models.news import News

class NewsRepository(ABC):
    @abstractmethod
    def create(self, news: News): pass

    @abstractmethod
    def list(self) -> list[News]: pass

    @abstractmethod
    def like(self, news_id: str) -> News | None: pass
