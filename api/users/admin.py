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



# from django.contrib import admin
# from django.contrib.admin import AdminSite
# from django.urls import reverse
# from django.http import HttpResponseRedirect
# from .models import CustomUser
# from mozilla_django_oidc.auth import OIDCAuthenticationBackend
# from mozilla_django_oidc import views as oidc_views  # Correct import

# # Regular Django admin (for superusers)
# admin.site.site_header = "Django Administration"

# # Custom OIDC Admin Site (Single definition)
# class OIDCAdminSite(AdminSite):
#     site_header = "Secure OIDC Admin"
    
#     def has_permission(self, request):
#         return (
#             request.user.is_active and
#             request.user.is_authenticated and
#             'admin' in request.user.roles
#         )

#     def login(self, request, extra_context=None):
#         """Override login to use OIDC flow"""
#         return oidc_views.OIDCAuthenticationRequestView.as_view()(request)

# # Create OIDC admin instance
# oidc_admin_site = OIDCAdminSite(name='oidc_admin')

# # Custom User Admin for both admin sites
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'oidc_id', 'is_admin')

# # Register with both admin interfaces
# admin.site.register(CustomUser, CustomUserAdmin)
# oidc_admin_site.register(CustomUser, CustomUserAdmin)










# from django.contrib import admin
# from django.contrib.admin import AdminSite
# from .models import CustomUser
# from mozilla_django_oidc.auth import OIDCAuthenticationBackend

# # admin.py
# from django.contrib import admin
# from django.contrib.admin import AdminSite
# from mozilla_django_oidc.auth import OIDCAuthenticationBackend

# # Regular Django admin (for superusers)
# admin.site.site_header = "Django Administration"

# # Custom OIDC Admin Site
# class OIDCAdminSite(AdminSite):
#     site_header = "Secure OIDC Admin"
    
#     def has_permission(self, request):
#         return (
#             request.user.is_active and
#             request.user.is_authenticated and
#             'admin' in request.user.roles
#         )

#     def login(self, request, extra_context=None):
#         """Override login to use OIDC flow"""
#         return oidc_views.OIDCAuthenticationRequestView.as_view()(request)

# oidc_admin_site = OIDCAdminSite(name='oidc_admin')

# # Default Admin (for superuser access)
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'oidc_id', 'is_admin')
#     # Regular Django admin functionality

# # Secure OIDC Admin Site (for role-based access)
# class OIDCAdminSite(AdminSite):
#     def has_permission(self, request):
#         return (
#             request.user.is_active and 
#             request.user.is_authenticated and
#             'admin' in request.user.roles  # OIDC role check
#         )

# oidc_admin_site = OIDCAdminSite(name='oidc_admin')

# # Explicitly register models with OIDC admin
# oidc_admin_site.register(CustomUser, CustomUserAdmin)

