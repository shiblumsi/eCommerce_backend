from rest_framework import serializers
from .models import *



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

    def validate_name(self, value):
        if Brand.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Brand Name Already Exists")
        return value

    def create(self, validated_data):
        name = validated_data.pop('name')
        brand = Brand.objects.create(name=name)
        return brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def validate_name(self, value):
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Category Name Already Exists")
        return value

    def create(self, validated_data):
        name = validated_data.pop('name')
        category = Category.objects.create(name=name)
        return category


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']

    def validate_name(self, value):
        if Color.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Color Name Already Exists")
        return value

    def create(self, validated_data):
        name = validated_data.pop('name')
        color = Color.objects.create(name=name)
        return color


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name']

    def validate_name(self, value):
        if Size.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Size Name Already Exists")
        return value

    def create(self, validated_data):
        name = validated_data.pop('name')
        size = Size.objects.create(name=name)
        return size


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



    
class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'is_active', 'category', 'brand']



class ProductDetailsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    product_items = ProductItemSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'is_active', 'category', 'brand', 'product_items']
    
    