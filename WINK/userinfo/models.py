from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, password):


        user = self.model(
            name=name,
            password=password
        )

        user.set_password(password)
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password):
        user = self.create_user(
            name = name,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)

        user.save(using=self._db)
        return user

    # def create_kakao_user(self, user_pk, extra_data):
    #     user = User.objects.get(pk=user_pk)
    #
    #     user.name = extra_data['properties']['nickname'] + str(extra_data['id'])
    #     user.image = extra_data['properties']['profile_image']
    #     user.save(using=self._db)
    #     return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20, null=True, unique=True)
    password = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    token = Token
    objects = UserManager()
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'

    def __str__(self):
        #return str(self.id)
        return str(self.name)