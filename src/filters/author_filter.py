from src.filters.base_strategy import FilterStrategy

class AuthorFilter(FilterStrategy):
    def apply(self, news_list, params):
        author_id = params.get("author_id")
        if not author_id:
            return news_list
        return [news for news in news_list if news.author_id == int(author_id)]
