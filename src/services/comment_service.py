import uuid
from src.models.comment import Comment
from src.repositories.memory.comment_repository import InMemoryCommentRepository

class CommentService:
    def __init__(self):
        self.repo = InMemoryCommentRepository()
    
    def create_comment(self, content:str, news_id:int, user_id:int ) -> Comment:
        comment_id = str(uuid.uuid4())
        comment = Comment(content=content, news_id=news_id, comment_id=comment_id,user_id=user_id)
        
        self.repo.create(comment)
        return comment
    
    def list_comments(self, news_id: str) -> list[Comment]:
        return self.repo.list_by_news(news_id)

        
  