from django.contrib import admin

# Register your models here.
from userinfo.models import NormalUser

admin.site.register(NormalUser)
