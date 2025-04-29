from abc import ABC, abstractmethod
from src.models.category import Category

class CategoryRepository(ABC):
    @abstractmethod
    def create(self, category: Category): pass

    @abstractmethod
    def list(self) -> list[Category]: pass
