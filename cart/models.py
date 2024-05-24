from django.db import models
from ecommerce_backend.utils import BaseModel
from account.models import CustomUser
from product.models import ProductItem,Product

# Create your models here.
class Cart(BaseModel):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE,related_name='product_items')
    quantity = models.PositiveIntegerField(default=1)