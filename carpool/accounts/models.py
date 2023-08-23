from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(
        unique=True,
        max_length=50,
        null=False
    )
    email = models.EmailField(
        unique=True,
        max_length=50,
        null=False,
        default="yourmail@duksung.ac.kr"
    )
    signup_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(
        max_length=50,
        null=False
    )