from flask import Flask
from src.main.routes.user_routes import user_bp
from src.main.routes.category_routes import category_bp
from src.main.routes.news_routes import news_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(category_bp)
app.register_blueprint(news_bp)