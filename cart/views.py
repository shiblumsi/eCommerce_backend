from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView, RetrieveAPIView,UpdateAPIView
from .serializers import CartItemSerializer,CartSerializer,IncreseDecreseQuantity
from django.shortcuts import get_object_or_404
from .models import CartItem, Cart
from product.models import ProductItem
from rest_framework.response import Response
from rest_framework import status

class AddToCartView(CreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = CartItem.objects.filter(cart__user=user)
    #     return queryset

    def perform_create(self, serializer):
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        product_item_id = self.request.data.get('product_item')
        product_item_obj = get_object_or_404(ProductItem, pk=product_item_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_item=product_item_obj,
            defaults={'quantity': self.request.data.get('quantity')}
        )

        if not created:
            cart_item.quantity += int(self.request.data.get('quantity'))
            cart_item.save()

        serializer.instance = cart_item
        serializer.save()


class CartView(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        user = self.request.user
        cart = get_object_or_404(Cart, user=user)
        return cart

class IncreaseQuantity(UpdateAPIView):
    serializer_class = IncreseDecreseQuantity

    def get_object(self):
        kwargs = {
            "pk": self.kwargs.get("pk", None)
        }
        cart_item = get_object_or_404(CartItem, **kwargs)
        print(cart_item.quantity)
        
        return cart_item

    def perform_update(self, serializer):
        cart_item = self.get_object()
        cart_item.quantity += 1
        cart_item.save()
        
        serializer.instance = cart_item
        serializer.save()


class DecreaseQuantity(UpdateAPIView):
    serializer_class = IncreseDecreseQuantity

    def get_object(self):
        kwargs = {
            "pk": self.kwargs.get("pk", None)
        }
        cart_item = get_object_or_404(CartItem, **kwargs)
        print(cart_item.quantity)
        
        return cart_item

    def perform_update(self, serializer):
        cart_item = self.get_object()
        cart_item.quantity -= 1
        
        if cart_item.quantity <= 0:
            cart_item.delete()
        else:
            cart_item.save()
        
        serializer.instance = cart_item
        serializer.save()