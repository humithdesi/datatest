from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
def TestSlide(request):
    try:
        return render(request,'datatest/SlideProDuct\TestSlide.htm')
    except:
        return Http404('Trang Không Tồn Tại')