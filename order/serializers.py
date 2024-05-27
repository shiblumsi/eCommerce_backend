from rest_framework import serializers
from .models import *



class OrderSerializer(serializers.ModelSerializer):
    payment_method = serializers.PrimaryKeyRelatedField(write_only=True,queryset=PaymentMethod.objects.all())
    shipping_info = serializers.PrimaryKeyRelatedField(write_only=True, queryset=ShippingInfo.objects.none())
    class Meta:
        model = Order
        fields = ['payment_method','shipping_info']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['shipping_info'].queryset = ShippingInfo.objects.filter(address__user=user)