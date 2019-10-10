

from django.urls import path
from login import views, api

urlpatterns = [
    path('', views.index),
    path('logincheck/',views.Login),
    path('afterlogin/',views.afterLogin),
    path('api/',api.create),
    path('api/logincheck/', api.logincheck),
    path('api/getuserinfo/', api.get_user_info),
]
