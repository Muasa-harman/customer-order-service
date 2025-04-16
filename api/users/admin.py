from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import CustomUser
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from mozilla_django_oidc import views as oidc_views

class OIDCAdminSite(AdminSite):
    def has_permission(self, request):
        return (
            request.user.is_active and
            request.user.is_authenticated and
            request.user.is_admin
        )

    def login(self, request, extra_context=None):
        return oidc_views.OIDCAuthenticationRequestView.as_view()(request)

oidc_admin_site = OIDCAdminSite(name='oidc_admin')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'oidc_id', 'is_admin')
    search_fields = ('email', 'oidc_id')

# Register models with both admin sites
oidc_admin_site.register(CustomUser, CustomUserAdmin)

