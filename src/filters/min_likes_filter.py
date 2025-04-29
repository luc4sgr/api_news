from src.filters.base_strategy import FilterStrategy

class MinLikesFilter(FilterStrategy):
    def apply(self, news_list, params):
        min_likes = params.get("min_likes")
        if not min_likes:
            return news_list
        return [news for news in news_list if news.likes >= int(min_likes)]
