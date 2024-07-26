import json
from urllib.request import urlopen
from functools import wraps
from flask import request
from jose import jwt
from setting import auth0_domain, api_audience

AUTH0_DOMAIN = auth0_domain
ALGORITHMS = ['RS256']
API_AUDIENCE = api_audience


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    auth = request.headers.get('Authorization', None)
    if not auth:
        raise AuthError({
            'status': False,
            'code': 'not_authorization'
        }, 401)
    
    parts_token = auth.split(' ')
    
    if len(parts_token) != 2 or parts_token[0] != 'Bearer':
        raise AuthError({
            'status': False,
            'code': 'invalid_token'
        }, 401)

    return parts_token[1]


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'status': False,
            'code': 'invalid_permissions'
        }, 400)
    
    if permission not in payload['permissions']:
        raise AuthError({
            'status': False,
            'code': 'unauthorized'
        }, 403)

    return True


def verify_decode_jwt(token):
    json_url = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(json_url.read())
    unverified_header = jwt.get_unverified_header(token)
    
    if 'kid' not in unverified_header:
        raise AuthError({
            'status': False,
            'code': 'invalid_token'
        }, 401)

    rsa_key = {}
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
            break

    if not rsa_key:
        raise AuthError({
            'status': False,
            'code': 'invalid_token'
        }, 401)

    try:
        return jwt.decode(token, rsa_key, algorithms=ALGORITHMS, audience=API_AUDIENCE, issuer=f'https://{AUTH0_DOMAIN}/')
    except jwt.ExpiredSignatureError:
        raise AuthError({
            'status': False,
            'code': 'token_expired'
        }, 401)
    except jwt.JWTClaimsError:
        raise AuthError({
            'status': False,
            'code': 'invalid_claim'
        }, 401)
    except Exception as ex:
        raise AuthError({
            'status': False,
            'code': 'invalid_token'
        }, 401)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator

