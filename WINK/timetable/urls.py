

from django.urls import path

from django.conf.urls import include

from timetable import views

urlpatterns = [
    path('', views.index),

]
