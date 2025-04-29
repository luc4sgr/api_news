from flask import jsonify
from app.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_errors(error):
        if isinstance(error, HttpUnprocessableEntityError):
            return jsonify({
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }), error.status_code

        # Erros genéricos (500)
        return jsonify({
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }), 500
