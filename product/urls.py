from django.urls import path
from .views import ProductCreateView,SizeListCreateView,SizeRetrieveUpdateDestroyView,ColorListCreateView,ColorRetrieveUpdateDestroyView, CategoryListView, BrandListView, SizeListView, ColorListView,ProductListView, ProductDetailView,BrandListCreateView,BrandRetrieveUpdateDestroyView,CategoryListCreateView, CategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category-list-create/', CategoryListCreateView.as_view(), name='category-list'),
    path('category/<pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-list'),

    path('brand-list-create/', BrandListCreateView.as_view(), name='brand-list-create'),
    path('brand/<pk>', BrandRetrieveUpdateDestroyView.as_view(), name='brand-pk'),
    path('brands/', BrandListView.as_view(), name='brand-list'),

    path('sizes/', SizeListView.as_view(), name='size-list'),
    path('size-list-create/', SizeListCreateView.as_view(), name='size-list-create'),
    path('size/<pk>/', SizeRetrieveUpdateDestroyView.as_view(), name='size-pk'),
    
    path('colors/', ColorListView.as_view(), name='color-list'),
    path('color-list-create/', ColorListCreateView.as_view(), name='color-list-create'),
    path('color/<pk>/', ColorRetrieveUpdateDestroyView.as_view(), name='color-pk'),
    
    path('pc/', ProductCreateView.as_view(), name='product-create'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('p/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]
