from django.http import Http404
from django.shortcuts import render,redirect

from dulieu.Views.Product.V_ProductDetail import ProductDetail
from ...Models.M_Product import Product
def CardProduct(request):
    if request.method=='POST':
        ProductNumber=request.POST.get('ProductNumber')
        ProductName=request.POST.get('ProductName')
        ProductDoDay=request.POST.get('ProductDoDay')
        ProductKichThuoc=request.POST.get('ProductKichThuoc')
        product=Product.objects.get(name=ProductName)
        card=request.session.get('card',{})
        request.session['card']=card
        if ProductName:
            card[ProductName]={
            'ProductName':ProductName,
            'ProductPrice':product.price,
            'ProductNumber':ProductNumber,
            'ProductDoDay':ProductDoDay,
            'ProductThuongHieu':str(product.thuongHieu),
            'ProductKichThuoc':ProductKichThuoc,
            'ProductChatLieu':str(product.chatLieu)
            }

        products=request.session['card']
        content={'products':products}
        return render(request, 'Product/CardProduct.htm',content)
    else:
        try:
            delProduct=request.GET.get('ProductName')
            print(delProduct)
            card=request.session.get('card',{})
            request.session['card']=card
            if delProduct:
                del request.session['card'][delProduct]
                return redirect('cardpage')
            products=request.session['card'].values()
            thongbao=len(products)
            content={'products':products,'thongbao':thongbao}
            
            return render(request, 'Product/CardProduct.htm',content)
        except:
            return Http404('Trang Không Tồn Tại')    