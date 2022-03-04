from distutils.log import error
from itertools import count
import re
from django.shortcuts import render,redirect
from django.http import Http404
from ...Models.M_Product import Product,Review

def testfileDetail(request, slug):
        if request.method=="POST":
                print('test thanh cong',slug)
        error=None
        producttest=Product.objects.get(slug=slug)
        error='lỗi rồi'    
        content={'producttest':producttest,'error':error}
        return render(request,'testfile/testfiledetail.html', content)