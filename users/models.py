from django.db import models
from  django.contrib.auth.models import AbstractUser
from  django.contrib.auth.models import User

# Create your models here.
class User(AbstractUser):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=200, unique=True)
  password = models.CharField(max_length=100)
  username= None

  USENAME_FIELD= 'email'
  REQUIRED_FIELDS=[]
