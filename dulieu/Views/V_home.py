from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
def Home(request):
    try:
        return render(request,'home.htm')
    except:
        raise Http404('Trang Không tồn tại')