from django import template

register=template.Library()

@register.inclusion_tag('dulieu/menu/MenuTop.htm',)
def MenuTop():

    posts=0
    content = {'posts': posts}
    return content
