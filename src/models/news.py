class News:
    def __init__(self, news_id: str, title: str, content: str, author_id: str, category: str, likes: int = 0):
        self.news_id = news_id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.category = category
        self.likes = likes
        
    def to_dict(self):
        return {
            "news_id": self.news_id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "category": self.category,
            "likes": self.likes
        }    