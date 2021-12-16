from django.shortcuts import render
from ..Models.models import HocSinh
# Create your views here.
def Home(request):
    hosinhs=HocSinh.objects.all()
    content={'hocsinhs':hosinhs}
    return render(request,'home.htm',content)