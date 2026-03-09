from django import template

register = template.Library()

@register.simple_tag
def in_basket(request, product_id):
    basket = request.session.get('basket', {})
    return str(product_id) in basket


@register.filter
def discount_price(price, discount):
    return round(float(price) * (1 - discount / 100), 2)