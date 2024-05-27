from django.contrib import admin
from .models import Address, Order, OrderItem, PaymentMethod, ShippingInfo
# Register your models here.


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city', 'state', 'zip_code']


@admin.register(ShippingInfo)
class ShippingInfoModelAdmin(admin.ModelAdmin):
    list_display = ['address', 'name', 'phone']


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'shipping_info', 'payment_method', 'delivery_charge', 'discount', 'cart_total', 'payable_amount', 'status', 'is_paid']


@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_item', 'quantity', 'total']


@admin.register(PaymentMethod)
class PaymentMethodModelAdmin(admin.ModelAdmin):
    list_display = ['payment_type']