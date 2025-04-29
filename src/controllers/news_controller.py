from flask import request, jsonify
from src.services.news_service import NewsService
from src.validators.news_validator import validate_create_news
from src.filters.strategy_manager import FilterManager
from src.filters.order_manager import order_news
from src.utils.paginator import paginate
from src.cache.news_cache import news_cache

class NewsController:
    def __init__(self):
        self.news_service = NewsService()

    def create(self):
        data = validate_create_news(request)
        news = self.news_service.create_news(**data)

        news_cache.clear()  # Limpa cache após criação
        return jsonify(news.to_dict()), 201

    def list(self):
        params = request.args.to_dict(flat=True)
        cache_key = str(sorted(params.items()))

        if cache_key in news_cache:
            print("✅ Servindo do cache")
            return jsonify(news_cache[cache_key]), 200

        news_list = self.news_service.list_news()
        filtered = FilterManager().apply_filters(news_list, params)
        ordered = order_news(
            filtered,
            params.get("order_by", "likes"),
            params.get("order", "desc")
        )

        # Paginação
        page = int(params.get("page", 1))
        per_page = int(params.get("per_page", 10))
        paginated = paginate([n.to_dict() for n in ordered], page, per_page)

        news_cache[cache_key] = paginated  # ✅ Salva a versão paginada no cache
        print("🔥 Salvando no cache")
        return jsonify(paginated), 200

    def like(self, news_id: str):
        news = self.news_service.like_news(news_id)
        if not news:
            return jsonify({"error": "News not found."}), 404

        news_cache.clear()  # Limpa cache após like
        return jsonify(news.to_dict()), 200
