from django.urls import path
from .views import AddToCartView, CartView,IncreaseQuantity,DecreaseQuantity,RemoveCartItemView,DeleteCartView,CouponListCreateView,ApplyCouponView

urlpatterns = [
    path('add-to-cart', AddToCartView.as_view(), name='add-to-cart'),
    path('cart', CartView.as_view(), name='cart-view'),

    path('cart-items/increase/<pk>/', IncreaseQuantity.as_view(), name='cart-item-increase'),
    path('cart-items/decrease/<pk>/', DecreaseQuantity.as_view(), name='cart-item-decrease'),

    path('cart/item/remove/<int:pk>/', RemoveCartItemView.as_view(), name='remove-cart-item'),
    path('cart/items/delete/', DeleteCartView.as_view(), name='delete-cart-items'),


    path('coupon-list-create/', CouponListCreateView.as_view(), name='coupon-list-create'),
    path('cart/apply-coupon/', ApplyCouponView.as_view(), name='apply-coupon'),

]