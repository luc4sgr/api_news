from abc import ABC, abstractmethod

class FilterStrategy(ABC):
    @abstractmethod
    def apply(self, news_list: list, params: dict) -> list:
        pass
