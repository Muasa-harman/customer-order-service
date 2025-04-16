from django.urls import path
from .admin import admin, oidc_admin_site  # Make sure oidc_admin_site is imported
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


# from django.urls import path
# from .admin import admin, oidc_admin_site
# # from mozilla_django_oidc import views as oidc_views

# urlpatterns = [
#     path('oidc-admin/', admin_site.urls), 
#     path('django-admin/', admin.site.urls),

#      # Standard Django admin
#     path('django-admin/', admin.site.urls),
    
#     # Secure OIDC admin
#     path('oidc-admin/', oidc_admin_site.urls),


#     path('oidc/login/', oidc_views.OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
#     path('oidc/callback/', oidc_views.OIDCAuthenticationCallbackView.as_view(), name='oidc_callback'),
#     path('oidc/logout/', oidc_views.OIDCLogoutView.as_view(), name='oidc_logout'),
# ]