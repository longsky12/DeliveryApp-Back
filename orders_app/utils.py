from .models import Cart, CartItem

# 카트에 아이템이 있는지 확인
def cart_has_items(user):
    user_cart_exists = Cart.objects.filter(userId=user).exists()

    if user_cart_exists:
        cart_item_exists = CartItem.objects.filter(cartId__userId=user).exists()
        return cart_item_exists
    return False
