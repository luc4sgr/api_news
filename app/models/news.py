class News:
    def __init__(self, news_id: int, title: str, content: str, author_id: int, category: str, likes: int = 0):
        self.news_id = news_id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.category = category
        self.likes = likes
