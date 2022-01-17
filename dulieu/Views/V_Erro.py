from django.shortcuts import render
from django.http import HttpResponse


def Error(request, exception):
    return render(request, 'Error.htm',{'loi':exception})