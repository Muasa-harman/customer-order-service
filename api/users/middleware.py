from django.contrib.auth.models import AnonymousUser


class JWTAuthMiddleware:
    def resolve(self, next, root, info, **kwargs):
        request = info.context
        if not hasattr(request, 'user'):
            request.user = AnonymousUser()
        return next(root, info, **kwargs)