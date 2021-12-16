from django.urls import path
from .Views.V_home import Home
urlpatterns = [
    path('',Home,name='homepage')
]