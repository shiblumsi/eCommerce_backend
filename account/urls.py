from django.urls import path
from .views import VendorSignupView, CustomerSignupView,CustomerLoginView

urlpatterns = [
    path('vs',VendorSignupView.as_view(),name='vendor-signup'),
    path('cs',CustomerSignupView.as_view(),name='customer-signup'),
    path('cl',CustomerLoginView.as_view(),name='customer-login'),
]
