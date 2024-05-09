from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['uid','name','sub_category','image']


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['uid','name']


@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['uid','name']


@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['uid','name']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['uid','name','description']


@admin.register(ProductItem)
class ProductIteModelAdmin(admin.ModelAdmin):
    list_display = ['uid','stock_available','description','price','status','is_active','product','color', 'size']
    

@admin.register(ProductImage)
class ProductIteModelAdmin(admin.ModelAdmin):
    list_display = ['uid','product_item','image']

