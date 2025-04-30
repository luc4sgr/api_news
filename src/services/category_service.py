from src.models.category import Category
from src.repositories.database.category_repository import PostgresCategoryRepository
class CategoryService:
    def __init__(self):
        self.repo = PostgresCategoryRepository()
        
    def create_category(self, name:str) -> Category:
        category = Category(name=name)
        self.repo.create(category)
        return category
    
    def list_categories(self) -> list[Category]:
        return self.repo.list()
        
        