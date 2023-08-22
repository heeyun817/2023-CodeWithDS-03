from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(
        unique=True,
        max_length=50,
        null=False
    )
    Email = models.EmailField(
        unique=True,
        max_length=50,
        null=False
    )
    signup_date = models.DateTimeField(auto_now_add=True)