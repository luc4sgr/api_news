from app.models.news import News

class NewsService:
    def __init__(self):
        self.news: list[News] = []
    
    def create_news(self, author_id:int, category:str, content:str, title:str="") -> News:
        news_id = len(self.news) + 1
        news = News(news_id=news_id, author_id=author_id,category=category, content=content, likes=0, title=title )
        self.news.append(news)
        return news
    
    def list_news(self) -> list[News]:
        return self.news
    
    def like_news(self, news_id: int):
        for news in self.news:
            if news.news_id == news_id:
                news.likes += 1
                return news
        return None

