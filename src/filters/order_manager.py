def order_news(news_list, order_by="likes", order="desc"):
    reverse = True if order == "desc" else False
    if order_by in ["likes", "title", "author_id", "category"]:
        return sorted(news_list, key=lambda n: getattr(n, order_by), reverse=reverse)
    return news_list
