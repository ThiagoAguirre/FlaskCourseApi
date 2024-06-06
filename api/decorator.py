from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import make_response, jsonify, request
from .services.user_service import listUserApiKey


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['roles'] != 'admin':
            return make_response(jsonify(mensagem='Não é permitted esse recurse. Only administrators'), 403)
        else:
            return fn(*args, **kwargs)

    return wrapper


def api_key_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        api_key = request.args.get('api_key')
        if api_key and listUserApiKey(api_key):
            return fn(*args, **kwargs)
        else:
            return make_response(jsonify(mensagem='Não é permitido esse recurso. Apenas api_tokens válidos'), 401)

    return wrapper
