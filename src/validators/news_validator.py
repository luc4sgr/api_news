from src.validators.validator_handler import validate_request

def validate_create_news(request):
    schema = {
        "title": {"type": "string", "required": True, "empty": False},
        "content": {"type": "string", "required": True, "empty": False},
        "category": {"type": "string", "required": True, "empty": False},
        "author_id": {"type": "integer", "required": True}
    }
    return validate_request(schema, request)
