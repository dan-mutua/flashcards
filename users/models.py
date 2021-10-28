from django.db import models
from  django.contrib.auth.models import AbstractUser
from  django.contrib.auth.models import User
from helpers.models import TrackingModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (PermissionsMixin,UserManager,AbstractBaseUser)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import jwt
from django.conf import settings
from datetime import datetime,timedelta

# Create your models here.
class User(AbstractUser):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=200, unique=True)
  password = models.CharField(max_length=100)
  # username= None

  EMAIL_FIELD='email'
  USENAME_FIELD= 'email'
  REQUIRED_FIELDS=['']

  @property
  def token(self):
    token=jwt.encode({'username':self.username,'email':self.email,'exp':datetime.utcnow()+ timedelta(hours=48)}, settings.SECRET_KEY,alogarithm='HS256')

    return token


# class MyUserManager(UserManager):
#   def _create_user(self,username,email,password,**extra_fields):
#     if not username:
#       raise ValueError('Username must be set')

#     if not email:
#       raise ValueError('email must be set')  

#     email=self.normalize_email(email)  
#     username=self.model.normalize_username(username)
#     user=self.model(username=username,email=email,**extra_fields)
#     user.set_password(password)
#     user.save(using=self._db)
#     return user

#   def create_user(self,username,email,password=None,**extra_fields):
#     extra_fields.setdefault('is_staff',False)
#     extra_fields.setdefault('is_superuser',False)
#     return self._create_user(username,email,password,**extra_fields)  
    
#   def create_superuser(self,username,email, password=None,**extra_fields):
#     extra_fields.setdefault('is_staff',True)
#     extra_fields.setdefault('is_superuser',True)  

#     if extra_fields.get('is_staff')is not True:
#       raise ValueError('Superuser must have is_staff=True')