from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer, BrandSerializer, CategorySerializer, SizeSerializer,ProductDetailsSerializer, ColorSerializer,ProductListSerializer
from .models import Product, Category, Brand, Size, Color


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandListCreateView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class SizeListView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class SizeListCreateView(ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class SizeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    lookup_field = 'pk'

class ColorListView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorListCreateView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    lookup_field = 'pk'


class ProductCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # Save the validated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log the invalid data
            print("Invalid data:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_field = 'id'


