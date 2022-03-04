from itertools import count
import re
from django.shortcuts import render,redirect
from django.http import Http404
from ...Models.M_Product import Product,Review

def testfileList(request):
    products=Product.objects.all()
    content={'ok':'ok','products':products}
    return render(request, 'testfile/testfilelist.html', content)