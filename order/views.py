from rest_framework.generics import CreateAPIView
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404

class PlaceOrderView(CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        shipping_info = serializer.validated_data['shipping_info']
        payment_method = serializer.validated_data['payment_method']
        delivery_charge = 20
        order = Order.objects.create(
            user = user,
            shipping_info = shipping_info,
            payment_method = payment_method,
            delivery_charge = delivery_charge,
            discount = cart.discount,
            cart_total = cart.total,
        )
        for item in cart.cart_items.all():
            OrderItem.objects.create(
                order = order,
                product_item = item.product_item,
                quantity = item.quantity

            )
        cart.clean_cart()
        return serializer