from flask import Blueprint, request, jsonify
from app.services.news_service import NewsService
from app.validators.news_validator import validate_create_news

news_bp = Blueprint('news', __name__, url_prefix='/news')
news_service = NewsService()

@news_bp.route("",  methods=['POST'])
def create_news():
    data = validate_create_news(request)
    news = news_service.create_news(**data)
    
    return jsonify(news.to_dict()), 201
    
@news_bp.route('', methods=['GET'])
def news_list():
    news_list = news_service.news_list()
    result = [news.to_dict() for news in news_list]
    
    return jsonify(result), 200