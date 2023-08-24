from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
#class User(models.Model):
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

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        
# Add related_name to groups and user_permissions fields
User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'