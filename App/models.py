from django.db import models

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, default='male')
    created_at = models.DateTimeField(auto_now_add=True)

class UserToken(models.Model):
    username = models.CharField(max_length=100)
    token = models.CharField(max_length=100, blank=True)