from src.filters.base_strategy import FilterStrategy

class CategoryFilter(FilterStrategy):
    def apply(self, news_list, params):
        category = params.get("category")
        if not category:
            return news_list
        return [news for news in news_list if news.category.lower() == category.lower()]
