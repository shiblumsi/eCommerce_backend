from django.urls import path
from .views import AddToCartView, CartView,IncreaseQuantity,DecreaseQuantity

urlpatterns = [
    path('add-product-item', AddToCartView.as_view(), name='cart-create'),
    path('cart', CartView.as_view(), name='cart-view'),

    path('cart-items/<pk>/increase/', IncreaseQuantity.as_view(), name='cart-item-increase'),
    path('cart-items/<pk>/decrease/', DecreaseQuantity.as_view(), name='cart-item-decrease'),
]