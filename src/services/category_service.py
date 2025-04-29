from src.models.category import Category
from src.repositories.memory.category_repository import InMemoryCategoryRepository

class CategoryService:
    def __init__(self):
        self.repo = InMemoryCategoryRepository()
        
    def create_category(self, name:str) -> Category:
        category = Category(name=name)
        self.repo.create(category)
        return category
    
    def list_categories(self) -> list[Category]:
        return self.repo.list()
        
        