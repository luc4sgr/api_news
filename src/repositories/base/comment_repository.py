from abc import ABC, abstractmethod
from src.models.comment import Comment

class CommentRepository(ABC):
    @abstractmethod
    def create(self, comment: Comment): pass

    @abstractmethod
    def list_by_news(self, news_id: str) -> list[Comment]: pass
