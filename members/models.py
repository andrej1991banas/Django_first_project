
from django.db import models
from django.contrib.auth.models import AbstractUser



class Member(models.Model):
  username = models.CharField(max_length=255, unique=True, null=True)
  firstname = models.CharField(max_length=255, null=True)
  lastname = models.CharField(max_length=255, null=True)
  email = models.EmailField(max_length=255, unique=True, null=True)
  entries = models.IntegerField(default =0)
  joined_date = models.DateField(null=True)
  password = models.CharField(max_length=255, null=True)



