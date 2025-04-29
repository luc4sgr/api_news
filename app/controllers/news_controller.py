from flask import Blueprint, request, jsonify
from app.services.news_service import NewsService
from app.validators.news_validator import validate_create_news

news_bp = Blueprint('news', __name__, url_prefix='/news')
news_service = NewsService()

@news_bp.route("",  methods=['POST'])
def create_news():
    data = validate_create_news(request)
    news = news_service.create_news(**data)
    
    return jsonify({
       'news_id' : news.news_id,
       'title' : news.title,
       'content' : news.content,
       'author_id' : news.author_id,
       'category' : news.category,
       'likes' : news.likes,
    }), 201
    
@news_bp.route('', methods=['GET'])
def list_news():
    list_news = news_service.list_news()
    result = [{  'news_id' : news.news_id,
       'title' : news.title,
       'content' : news.content,
       'author_id' : news.author_id,
       'category' : news.category,
       'likes' : news.likes,} for news in list_news]
    
    return jsonify(result), 200