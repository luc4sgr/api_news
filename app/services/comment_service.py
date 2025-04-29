from app.models.comment import Comment

class CommentService:
    def __init__(self):
        self.comments: list[Comment] = []
    
    def create_comment(self, content:str, news_id:int, user_id:int ) -> Comment:
        comment_id = len(self.comments) + 1
        comment = Comment(content=content, news_id=news_id, comment_id=comment_id,user_id=user_id)
        self.comments.append(comment)
        return comment
    
    def comments_list(self, news_id: int) -> list[Comment]:
        comments: list[Comment] = []
        for comment in self.comments:
            if comment.news_id == news_id:
                comments.append(comment)

        return comments

        
  