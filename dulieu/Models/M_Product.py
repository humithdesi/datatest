from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class BoSuuTap(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.name

class ThuongHieu(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.name

class LoaiGa(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.name

class LoaiNem(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.name

class ChatLieu(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.name
class KichThuoc(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.name
class DoDay(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100,unique=True)
    price=models.IntegerField()
    discount=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to='ImageProduct')

    boSuuTap=models.ForeignKey(BoSuuTap,on_delete=models.CASCADE,default=None)
    thuongHieu=models.ForeignKey(ThuongHieu,on_delete=models.CASCADE,default=None)
    loaiGa=models.ForeignKey(LoaiGa,on_delete=CASCADE,default=None,blank=True,null=True)
    loaiNem=models.ForeignKey(LoaiNem,on_delete=models.CASCADE,default=None,blank=True,null=True)
    chatLieu=models.ForeignKey(ChatLieu,on_delete=models.CASCADE)

    kichThuoc=models.ManyToManyField(KichThuoc)
    doDay=models.ManyToManyField(DoDay)
    slug=models.SlugField(unique=True,null=True)
    def __str__(self):
        return self.name

