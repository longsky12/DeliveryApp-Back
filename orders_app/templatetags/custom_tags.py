from django import template

register = template.Library()

@register.filter
def calculate_total_price(cart_item):
    menu_price = cart_item.menuId.price
    quantity = cart_item.quantity
    option_price = cart_item.menuOptionId.price if cart_item.menuOptionId else 0
    return menu_price * quantity + option_price