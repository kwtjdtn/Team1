

from django.urls import path
from login import views
from api import api

urlpatterns = [
    path('', views.index),
    path('logincheck/',views.Login),
    path('afterlogin/',views.afterLogin),
    path('api/createschedule/',api.createschedule),
    path('api/getuserinfo/', api.get_user_info),
    path('api/test/', api.test),
    path('api/login/', api.ktislogin),
    path('api/multiply/', api.multiply),
]
