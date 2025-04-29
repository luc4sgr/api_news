from abc import ABC, abstractmethod

class NewsRepository(ABC):
    @abstractmethod
    def create(self, news): pass

    @abstractmethod
    def list(self): pass

    @abstractmethod
    def like(self, news_id): pass
