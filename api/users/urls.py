from django.urls import path
from .admin import admin, oidc_admin_site  
from mozilla_django_oidc import views as oidc_views

urlpatterns = [
    # OIDC Authentication Endpoints
    path('oidc/login/', oidc_views.OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
    path('oidc/callback/', oidc_views.OIDCAuthenticationCallbackView.as_view(), name='oidc_callback'),
    path('oidc/logout/', oidc_views.OIDCLogoutView.as_view(), name='oidc_logout'),
    
    # Admin Sites
    path('django-admin/', admin.site.urls),       # Standard Django admin
    path('oidc-admin/', oidc_admin_site.urls),    # Secure OIDC admin
]

