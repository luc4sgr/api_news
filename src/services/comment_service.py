from src.models.comment import Comment
import uuid

class CommentService:
    def __init__(self):
        self.comments: list[Comment] = []
    
    def create_comment(self, content:str, news_id:int, user_id:int ) -> Comment:
        comment_id = str(uuid.uuid4())
        comment = Comment(content=content, news_id=news_id, comment_id=comment_id,user_id=user_id)
        self.comments.append(comment)
        return comment
    
    def list_comments(self, news_id: int) -> list[Comment]:
        return [comment for comment in self.comments if comment.news_id == news_id]

        
  