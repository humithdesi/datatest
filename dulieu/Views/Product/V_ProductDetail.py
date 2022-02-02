from itertools import count
from django.shortcuts import render
from django.http import Http404
from ...Models.M_Product import Product
def ProductDetail(request, slug):
    try:
         product= Product.objects.get(slug=slug)
         product.count_view +=1
         product.save()
         print(product.count_view)
         sizes=product.kichThuoc.all()
         dodays=product.doDay.all()
    except Product.DoesNotExist:
        raise Http404('Sản Phẩm Không Tồn tại')

    return render(request, 'dulieu/Product/ProductDetail.htm', context={'product': product,'sizes':sizes,'dodays':dodays})