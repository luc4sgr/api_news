from src.models.user import User
import uuid

class UserService:
    def __init__(self):
        self.users: list[User] = []
        
    def  create_user(self, username:str):
        user_id = str(uuid.uuid4())
        user = User( user_id=user_id, username=username )
        self.users.append(user)
        
        return user
    
    def users_list(self):
        return self.users
