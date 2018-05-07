from django.db import models
from django.contrib import admin

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(db_column='username',max_length=32)
    password = models.CharField(db_column='password',max_length=128)
    email = models.EmailField(db_column='email',max_length=50)

admin.site.register(UserInfo)
