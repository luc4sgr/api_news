from app.controllers.user_controller import user_bp
from app.controllers.news_controller import news_bp
from app.controllers.comment_controller import comment_bp
from app.controllers.category_controller import category_bp

def init_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(category_bp)
