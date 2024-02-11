from django.db import models


# 用户登录信息
class UserCredentials(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True)


# 用户token
class UserToken(models.Model):
    username = models.CharField(max_length=100, unique=True)
    token = models.CharField(max_length=100, blank=True)


# 用户profile信息
class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    age = models.PositiveIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    preferred_address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, default='male')
    create_time = models.DateTimeField(auto_now_add=True)


# 存放头像信息
class UserAvatar(models.Model):
    username = models.CharField(max_length=100, unique=True)
    avatar_file_name = models.CharField(max_length=100)

