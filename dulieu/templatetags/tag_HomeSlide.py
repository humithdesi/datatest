from django import template
from ..Models.M_Product import Product

register=template.Library()

@register.inclusion_tag('datatest/Hometag/HomeSlide1.htm',)
def HomeSlide1():

    posts=0
    content = {'posts': posts}
    return content

@register.inclusion_tag('datatest/Hometag/HomeSlide2.htm',)
def HomeSlide2():
    products=Product.objects.all()[:4]
    content={'products':products}
    return content

@register.inclusion_tag('datatest/Hometag/HomeSlide3.htm',)
def HomeSlide3():
    products=Product.objects.all()[:4]
    content={'products':products}
    return content   