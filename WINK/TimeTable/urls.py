

from django.urls import path

from django.conf.urls import include

from TimeTable import views

urlpatterns = [
    path('', views.index),

]
