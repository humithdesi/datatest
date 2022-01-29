from django.shortcuts import render
from django.http import Http404
from ...Models.M_Product import Product
def ProductDetail(request, slug):
    try:
         product= Product.objects.get(slug=slug)
         sizes=product.kichThuoc.all()
         dodays=product.doDay.all()
    except Product.DoesNotExist:
        raise Http404('Sản Phẩm Không Tồn tại')

    return render(request, 'datatest/Product/ProductDetail.htm', context={'product': product,'sizes':sizes,'dodays':dodays})