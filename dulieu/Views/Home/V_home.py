from urllib import request
from django.shortcuts import render
# Create your views here.
def HomePage(request):
        a=12
        content={'a':a}
        return render (request,'dulieu/hometag/home1.html',content)
