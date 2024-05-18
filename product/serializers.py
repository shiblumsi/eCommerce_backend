from rest_framework import serializers
from .models import *



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['stock_available', 'description', 'price', 'color', 'size']


class ProductSerializer(serializers.ModelSerializer):
    product_items = ProductItemSerializer(many=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'brand', 'product_items']

    def create(self, validated_data):
        product_items_data = validated_data.pop('product_items')
        product = Product.objects.create(**validated_data)
        for product_item_data in product_items_data:
            product_item = ProductItem.objects.create(product=product,**product_item_data)
        return product



    