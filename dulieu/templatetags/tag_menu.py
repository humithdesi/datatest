from django import template

register=template.Library()

@register.inclusion_tag('dulieu/menu/Menu.htm',takes_context=True)
def Menu(context):
    session = context['request'].session
    
    if session['card']:
        countProduct=len(session['card'])
    else:
        countProduct=''  
    content={'countProduct':countProduct}
    return content
