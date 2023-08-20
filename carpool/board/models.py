from django.db import models

# Create your models here.
class board(models.Model):
    s_title = models.CharField(max_length=20)
    d_title = models.CharField(max_length=20)
    content = models.TextField()
    star = models.BooleanField(default=False)