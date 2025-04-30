from src.repositories.base.user_repository import UserRepository
from src.database.models.user_orm import UserORM
from src.database.config import SessionLocal

class PostgresUserRepository(UserRepository):
    def __init__(self):
        self.db = SessionLocal()

    def create(self, user):
        user_orm = UserORM(
            user_id=user.user_id,
            username=user.username
        )
        self.db.add(user_orm)
        self.db.commit()

    def list(self):
        return self.db.query(UserORM).all()
