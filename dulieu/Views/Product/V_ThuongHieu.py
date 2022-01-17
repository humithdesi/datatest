from django.shortcuts import render
from django_filters import filters
from ...Models.M_Product import Product
from ...FORMS.f_ProductFilter import ProductFilter
from django.http import HttpResponse,Http404
# Create your views here.
def ThuongHieu(request,slug):
    products=Product.objects.all().filter(thuongHieu__slug=slug)
    filters=ProductFilter(request.GET,queryset=products)
    content={'filters':filters}
    return render(request,'Product/ThuongHieu.htm',content)
