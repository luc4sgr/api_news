from app.validators.validator_handler import validate_request

def validate_create_user(request):
    schema = {
        "username": {"type": "string", "required": True, "empty": False}
    }
    return validate_request(schema, request)
