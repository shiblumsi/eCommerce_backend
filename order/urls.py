from django.urls import path
from .views import PlaceOrderView
urlpatterns = [
    path('po',PlaceOrderView.as_view(),name='place-order'),
]