from django.shortcuts import render
from django.http import HttpResponse


def Error(request, exception):
    return render(request, 'datatest/Error.htm',{'loi':exception})