from django import template
from ..Models.M_Product import Product

register=template.Library()

@register.inclusion_tag('dulieu/hometag/tintuc.htm',)
def TinTuc():

    posts=0
    content = {'posts': posts}
    return content

