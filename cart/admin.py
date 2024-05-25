from django.contrib import admin
from .models import Cart,CartItem
# Register your models here.

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['uid']



@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ['id','uid','cart','product_item','quantity']