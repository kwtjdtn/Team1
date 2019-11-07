from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _


class NormalUser(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    pw = models.CharField(max_length=20)
    token = models.CharField(max_length=550, unique=True, null=True)
    expire = models.CharField(max_length=100, null=True)

    def __str__(self):
        #return str(self.id)
        return str(self.id)
