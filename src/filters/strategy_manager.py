from src.filters.author_filter import AuthorFilter
from src.filters.category_filter import CategoryFilter
from src.filters.min_likes_filter import MinLikesFilter

class FilterManager:
    def __init__(self):
        self.strategies = [
            AuthorFilter(),
            CategoryFilter(),
            MinLikesFilter()
        ]

    def apply_filters(self, news_list, params):
        for strategy in self.strategies:
            news_list = strategy.apply(news_list, params)
        return news_list
