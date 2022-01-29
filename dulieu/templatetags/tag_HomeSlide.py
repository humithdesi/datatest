from django import template
from ..Models.M_Product import Product

register=template.Library()

@register.inclusion_tag('datatest/hometag/homeslide1.htm',)
def homeslide1():

    posts=0
    content = {'posts': posts}
    return content

@register.inclusion_tag('datatest/hometag/homeslide2.htm',)
def homeslide2():
    products=Product.objects.all()[:4]
    content={'products':products}
    return content

@register.inclusion_tag('datatest/hometag/homeslide3.htm',)
def homeslide3():
    products=Product.objects.all()[:4]
    content={'products':products}
    return content   