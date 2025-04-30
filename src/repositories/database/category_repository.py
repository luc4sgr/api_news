from src.repositories.base.category_repository import CategoryRepository
from src.database.models.category_orm import CategoryORM
from src.database.config import SessionLocal

class PostgresCategoryRepository(CategoryRepository):
    def __init__(self):
        self.db = SessionLocal()

    def create(self, category):
        category_orm = CategoryORM(name=category.name)
        self.db.add(category_orm)
        self.db.commit()

    def list(self):
        return self.db.query(CategoryORM).all()
