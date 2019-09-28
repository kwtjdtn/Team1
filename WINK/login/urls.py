

from django.urls import path

from django.conf.urls import include

from login import views

urlpatterns = [
    path('', views.index),
    path('logincheck/',views.Login)
]
