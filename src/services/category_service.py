from src.models.category import Category

class CategoryService:
    def __init__(self):
        self.categories: list[Category] = []
        
    def create_category(self, name:str) -> Category:
        category = Category(name=name)
        self.categories.append(category)
        return category
    
    def list_categories(self) -> list[Category]:
        return self.categories
        
        