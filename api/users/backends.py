from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class KeycloakOIDCBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super().create_user(claims)
        user.oidc_id = claims.get('sub')
        user.roles = claims.get('realm_access', {}).get('roles', [])
        user.save()
        return user

    def update_user(self, user, claims):
        user.oidc_id = claims.get('sub')
        user.roles = claims.get('realm_access', {}).get('roles', [])
        user.save()
        return user

    def filter_users_by_claims(self, claims):
        sub = claims.get('sub')
        return self.UserModel.objects.filter(oidc_id=sub)