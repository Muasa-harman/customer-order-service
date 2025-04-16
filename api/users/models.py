from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Add OIDC-specific fields
    oidc_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        help_text="OpenID Connect subject identifier"
    )
    roles = models.JSONField(
        default=list,
    )
    
    customer_profile = models.OneToOneField(
        'customers.Customer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='linked_user'
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        indexes = [
            models.Index(fields=['oidc_id']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return f"{self.email} ({self.oidc_id})"

    @property
    def is_admin(self):
        return 'admin' in self.roles
    

#     from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _

# class CustomUser(AbstractUser):
#     # Add OIDC-specific fields
#     oidc_id = models.CharField(
#         max_length=255,
#         unique=True,
#         blank=True,
#         help_text="OpenID Connect subject identifier"
#     )
#     roles = models.JSONField(
#         default=list,
#     )
    
#     customer_profile = models.OneToOneField(
#         'customers.Customer',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='linked_user'
#     )

#     class Meta:
#         verbose_name = _("User")
#         verbose_name_plural = _("Users")
#         indexes = [
#             models.Index(fields=['oidc_id']),
#             models.Index(fields=['email']),
#         ]

#     def __str__(self):
#         return f"{self.email} ({self.oidc_id})"

#     @property
#     def is_admin(self):
#         return 'admin' in self.roles