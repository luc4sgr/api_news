from sqlalchemy import Column, String
from src.database.config import Base

class CategoryORM(Base):
    __tablename__ = "categories"

    name = Column(String, primary_key=True)
