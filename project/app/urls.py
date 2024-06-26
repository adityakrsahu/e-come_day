from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    path("login/",login,name='login'),
    path("registration/",registration,name='registration'),
    path("profile/",profile,name='profile'),
    path("loginpage",loginpage,name='loginpage'),
    path("registerpage",registerpage,name='registerpage'),
    path('mobile',mobile,name='mobile')
]