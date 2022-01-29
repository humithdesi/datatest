import re
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django_filters import filters
from ...Models.M_Product import Product
from ...FORMS.f_ProductFilter import ProductFilter
from django.core.paginator import Paginator
# Create your views here.
def Nem(request):
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
            products=Product.objects.all().filter(price__gt=priceSelect).filter(loaiGa=None)
            filters=ProductFilter(request.GET,queryset=products)

            paginator_filter = Paginator(filters.qs,3) 

            page_number = request.GET.get('page')
            page_obj =paginator_filter.get_page(page_number)
            print(type(page_obj.paginator.num_pages))
            for i in range(page_obj.paginator.num_pages):
                print(1+i)

            listTest=[1+i for i in range (page_obj.paginator.num_pages ) ]  
            print(listTest) 
            content={'filters':filters,'priceSelect':priceSelect,'priceSelectText':priceSelectText,'page_obj': page_obj,'listTest':listTest}
            return render(request,'datatest/Product/Nem.htm',content)
        except :
            raise Http404()
        
