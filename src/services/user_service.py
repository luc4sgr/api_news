import uuid
from src.models.user import User
from src.repositories.memory.user_repository import InMemoryUserRepository

class UserService:
    def __init__(self):
        self.repo = InMemoryUserRepository()

    def create_user(self, username: str):
        user = User(user_id=str(uuid.uuid4()), username=username)
        self.repo.create(user)
        return user

    def list_users(self):
        return self.repo.list()
