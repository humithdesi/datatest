from django.http import Http404
from django.shortcuts import render
from django_filters import filters
from ...Models.M_Product import Product
from ...FORMS.f_ProductFilter import ProductFilter
# Create your views here.
def ChanGaGoi(request):
    try:
        priceSelectText=None
        priceSelect=request.GET.get('priceSelect',0)
        if priceSelect=='1':
            priceSelectText='1-500'
        elif priceSelect=='100' : 
            priceSelectText='100-500'
        elif priceSelect=='200':
            priceSelectText='200-500'
        print (priceSelect)
        products=Product.objects.all().filter(price__gt=priceSelect)
        filters=ProductFilter(request.GET,queryset=products)
        content={'filters':filters,'priceSelect':priceSelect,'priceSelectText':priceSelectText}
        return render(request,'Product/ChanGagoi.htm',content)
    except:
        return Http404  