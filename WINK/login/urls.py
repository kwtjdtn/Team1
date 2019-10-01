

from django.urls import path
from login import views, api

urlpatterns = [
    path('', views.index),
    path('logincheck/',views.Login),
    path('api/',api.create),
]
