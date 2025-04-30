from sqlalchemy import Column, String
from src.database.config import Base

class UserORM(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
