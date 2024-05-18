from django.urls import path
from .views import ProductCreateView,CategoryListView, BrandListView, SizeListView, ColorListView
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('sizes/', SizeListView.as_view(), name='size-list'),
    path('colors/', ColorListView.as_view(), name='color-list'),
    
    path('pc/', ProductCreateView.as_view(), name='product-create'),
]
