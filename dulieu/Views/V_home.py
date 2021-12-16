from django.shortcuts import render
from ..Models.models import HocSinh,Lop
# Create your views here.
def Home(request):
    hosinhs=HocSinh.objects.all()
    lops=Lop.objects.all()
    print('ok thanh cong roi')
    content={'hocsinhs':hosinhs,'lops':lops}
    return render(request,'home.htm',content)