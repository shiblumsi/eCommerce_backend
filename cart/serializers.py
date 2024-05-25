from rest_framework import serializers
from .models import Cart, CartItem, Coupon
from product.models import ProductItem



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_item','quantity']


class CartItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product_item','quantity','unite_price','total_price']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemDetailSerializer(many=True, read_only=True)
    coupon = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Cart
        fields = ['user', 'total', 'cart_items', 'coupon', 'discount', 'payable_amount']

    def update(self, instance, validated_data):
        coupon_code = validated_data.get('coupon', None)
        if coupon_code:
            coupon = Coupon.objects.filter(code=coupon_code, is_active=True).first()
            print('ssssssssssssssssssssss',coupon)
            if not coupon:
                raise serializers.ValidationError({"coupon": "Invalid or inactive coupon"})
            instance.coupon = coupon
        else:
            instance.coupon = None
        
        instance.save()
        instance.update_total()
        return instance

class IncreaseDecreaseQuantity(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = []

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'discount']

class CouponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code']