from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from flask import Request

def validate_request(schema: dict, request: Request) -> dict:
    validator = Validator(schema)
    body = request.get_json() or {}

    if not validator.validate(body):
        raise HttpUnprocessableEntityError(str(validator.errors))

    return body  # Retorna o body validado
