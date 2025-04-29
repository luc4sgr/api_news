from app.validators.validator_handler import validate_request

def validate_create_category(request):
    schema = {
        "name": {"type": "string", "required": True, "empty": False}
    }
    return validate_request(schema, request)
