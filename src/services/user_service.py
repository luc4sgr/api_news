import uuid
from src.models.user import User
from src.repositories.database.user_repository import PostgresUserRepository
class UserService:
    def __init__(self):
        self.repo = PostgresUserRepository()

    def create_user(self, username: str):
        user = User(user_id=str(uuid.uuid4()), username=username)
        self.repo.create(user)
        return user

    def list_users(self):
        return self.repo.list()
