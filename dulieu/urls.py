from django.urls import path
from .Views.V_home import Home
from .Views.V_TestSlide import TestSlide
from .Views.V_auth import LoginPage,ResignPage,LogOutPage
urlpatterns = [
    path('',Home,name='homepage'),
    path('test',TestSlide,name='testpage'),
    path('login',LoginPage,name='loginpage'),
    path('resign',ResignPage,name='resignpage'),
    path('logout',LogOutPage,name='logoutpage')
]