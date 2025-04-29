from abc import ABC, abstractmethod
from src.models.user import User

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User): pass

    @abstractmethod
    def list(self) -> list[User]: pass
