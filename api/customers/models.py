from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):
    user = models.OneToOneField(
        'users.CustomUser',  
        on_delete=models.CASCADE,
        related_name='customer_account',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', "Invalid phone format.")]
    )

    def __str__(self):
        return self.name


# from django.db import models
# from django.core.validators import RegexValidator

# class Customer(models.Model):
#     #  update
#      user = models.OneToOneField(
#         'auth.CustomUser',
#         on_delete=models.CASCADE,
#         related_name='customer_profile',
#         null=True,
#         blank=True
#     )
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=20, unique=True)
#     phone = models.CharField(
#         max_length=20,
#         blank=True,
#         null=True,
#         validators=[RegexValidator(r'^\+?1?\d{9,15}$', "Invalid phone format.")]
#     )

#     def __str__(self):
#         return self.name
