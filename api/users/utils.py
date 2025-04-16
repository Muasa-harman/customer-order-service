from datetime import datetime

from django.conf import settings


def jwt_payload_handler(user, context=None):
    return {
        'user_id': user.id,
        'email': user.email,
        'roles': user.roles,
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
    }