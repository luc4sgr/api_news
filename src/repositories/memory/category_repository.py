from src.repositories.base.category_repository import CategoryRepository
from src.models.category import Category

class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self):
        self.categories: list[Category] = []

    def create(self, category: Category):
        self.categories.append(category)

    def list(self) -> list[Category]:
        return self.categories
