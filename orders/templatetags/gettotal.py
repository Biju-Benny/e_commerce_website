from django import template

register = template.Library()

@register.simple_tag(name='gettotal')
def gettotal(cart):
    total = 0 
    for item in cart.aded_items.all():
        total += item.quantity*item.product.price 
    return total

