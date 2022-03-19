from django import template

register=template.Library()

@register.inclusion_tag('dulieu/menu/Menu.htm',takes_context=True)
def Menu(context):
    user=context['user'] # muốn dùng user trong thẻ mẫu inclusion_tag phải gọi bằng contexts
    content={'user':user}
    return content
