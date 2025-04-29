from flask import Flask
from app.errors.handle_errors import register_error_handlers
def create_app():
    app = Flask(__name__)

    from app.routes import init_routes
    init_routes(app)

    register_error_handlers(app)

    return app