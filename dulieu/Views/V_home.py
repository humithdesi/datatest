from django.shortcuts import render
from ..Models.models import HocSinh
# Create your views here.
def Home(request):
    hosinhs=HocSinh.objects.all()
    print('ok thanh cong roi')
    content={'hocsinhs':hosinhs}
    return render(request,'home.htm',content)