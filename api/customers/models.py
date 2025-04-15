from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)  

    def __str__(self):
        return self.name