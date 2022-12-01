from blog import app
from marshmallow import Schema, fields, ValidationError
from functools import wraps
from flask import request, jsonify


class ArticleSchema(Schema):
    id = fields.Int(required=False)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    content = fields.Str(required=True)



def validate_request(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                schema.validate(request.json)
            except ValidationError as e:
                error = {
                    "status": "error",
                    "messages": f"{e.field_name} is invalid"
                }
                return jsonify(error), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator

            