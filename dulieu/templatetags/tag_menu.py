from django import template

register=template.Library()

@register.inclusion_tag('dulieu/menu/Menu.htm',takes_context=True)
def Menu(context):
    session = context['request'].session #muốn dùng request trong thẻ mẫu inclusion_tag phải gọi bằng context
    user=context['user'] # muốn dùng user trong thẻ mẫu inclusion_tag phải gọi bằng context
    countProduct=len(session['card'])
    content={'user':user,'countProduct':countProduct}
    return content
