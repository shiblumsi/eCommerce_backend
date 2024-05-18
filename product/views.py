from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer, BrandSerializer, CategorySerializer, SizeSerializer, ColorSerializer
from .models import Product, Category, Brand, Size, Color


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SizeListView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class ColorListView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


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


