from rest_framework import serializers
from .models import Cart, CartItem
from product.models import ProductItem



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_item','quantity']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['user','cart_items']

class IncreseDecreseQuantity(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = []

