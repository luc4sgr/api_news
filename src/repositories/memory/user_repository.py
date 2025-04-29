from src.repositories.base.user_repository import UserRepository
from src.models.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: list[User] = []

    def create(self, user: User):
        self.users.append(user)

    def list(self) -> list[User]:
        return self.users
