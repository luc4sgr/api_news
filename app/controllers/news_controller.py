from flask import Blueprint, request, jsonify
from app.services.news_service import NewsService

news_bp = Blueprint('news', __name__, url_prefix='/news')
news_service = NewsService()

@news_bp.route("",  methods=['POST'])
def create_news():
    data = request.get_json()
    author_id = data.get('author_id')
    category = data.get('category')
    content = data.get('content')
    title = data.get('title')
    news = news_service.create_news(
        author_id=author_id,
        category=category,
        content=content,
        title=title
        )
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
    list_news = news_service.like_news()
    result = [{  'news_id' : news.news_id,
       'title' : news.title,
       'content' : news.content,
       'author_id' : news.author_id,
       'category' : news.category,
       'likes' : news.likes,} for news in list_news]
    
    return jsonify(result), 200