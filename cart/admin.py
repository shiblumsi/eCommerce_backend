from django.contrib import admin
from .models import Cart,CartItem, Coupon
# Register your models here.

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['uid','user']



@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ['id','uid','cart','product_item','quantity']


@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['uid', 'code', 'discount', 'is_active']