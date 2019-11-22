from django.conf.urls import url

from movies.api.viewset import *
from django.urls import path

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('user/', user_view, name="user_view")
]