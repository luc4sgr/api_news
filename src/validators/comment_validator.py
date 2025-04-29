from src.validators.validator_handler import validate_request

def validate_create_comment(request):
    schema = {
        "content": {"type": "string", "required": True, "empty": False},
        "news_id": {"type": "string", "required": True},
        "user_id": {"type": "string", "required": True}
    }
    return validate_request(schema, request)
   