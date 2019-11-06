from django.contrib import admin

# Register your models here.
from userinfo.models import User, NormalUser

admin.site.register(User)
admin.site.register(NormalUser)