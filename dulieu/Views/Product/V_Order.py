from email.headerregistry import Address
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from ...Models.M_Product import Product
from ...Models.M_Order import Order
from django.http import HttpResponse
def OrderProduct(request):
    if request.method=='POST':
        current_user=None 
        if request.user.is_authenticated:
            current_user=request.user
               
        Address=request.POST.get('Address')
        Phone=request.POST.get('Phone')
        products=request.session['card'].values()
        Test=request.session['card'].keys()
        for i in products:
            sanpham=Product.objects.get(name=i['ProductName'])
            sum=int(i['ProductPrice'])* int(i['ProductNumber'])
            order=Order(
                product=Product(id=sanpham.id),
                doday=i['ProductDoDay'],
                price=int(i['ProductPrice']),
                quantity=int(i['ProductNumber']),
                user=current_user,
                address=Address,
                phone=int(Phone),
                total=int(sum)
            )
            order.save()

        request.session['card']={}
            

       
           
        return HttpResponse('Order Thanh Cong')