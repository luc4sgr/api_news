from app.models.user import User

class UserService:
    def __init__(self):
        self.users: list[User] = []
        
    def  create_user(self, username:str):
        user_id = len(self.users) + 1
        user = User( user_id=user_id, username=username )
        self.users.append(user)
        
        return user
    
    def list_users(self):
        return self.users
