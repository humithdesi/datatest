from itertools import count
import re
from django.shortcuts import render,redirect
from django.http import Http404
from ...Models.M_Product import Product,Review

def ProductDetail(request, slug):
    if request.method=='POST':
       #Post Comment
        productCommnet=Product.objects.get(slug=slug)
        user=request.user
        Comment=request.POST.get('comment')
        if Comment:
            review=Review(product=productCommnet,user=user,comment=Comment)
            review.save()
        else:
            print('khong thanh cong')
    
        print(Comment)
        print('test')
        return redirect('productdetail',slug=slug)
    else:
        try:
            product= Product.objects.get(slug=slug) 
            product.count_view +=1
            product.save()
            print(product.count_view)
            sizes=product.kichThuoc.all()
            dodays=product.doDay.all()
            products=Product.objects.all()
            comments = product.comments.all()# product.relate_name.all() truy vấn liên quan đến khóa chính product
        except Product.DoesNotExist:
            raise Http404('Sản Phẩm Không Tồn tại')
        content={
        'product': product,
        'sizes':sizes,
        'dodays':dodays,
        'products':products,
        'comments':comments
        }    

        return render(request, 'dulieu/Product/ProductDetail.htm', content)