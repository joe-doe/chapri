from flask import jsonify, request
from functools import wraps


def check_auth(username, password):
    return username == 'admin' and password == 'secret'


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            message = {'error': 'Basic Auth Required.'}
            resp = jsonify(message)
            resp.status_code = 401
            return resp

        return f(*args, **kwargs)
    return decorated
