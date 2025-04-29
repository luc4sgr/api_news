class Comment:
    def __init__(self, comment_id: int, news_id: int, user_id: int, content: str):
        self.comment_id = comment_id
        self.news_id = news_id
        self.user_id = user_id
        self.content = content
        
    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "news_id": self.news_id,
            "user_id": self.user_id,
            "content": self.content
        }
