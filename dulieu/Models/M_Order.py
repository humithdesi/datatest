from datetime import datetime
from email.headerregistry import Address
import re
from django.db import models

from ..Models.M_Product import Product
from django.contrib.auth.models import User
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    doday=models.CharField(max_length=50,null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,default=None,null=True)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    total=models.IntegerField(null=True)
    
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.address