from django.db import models
from ecommerce_backend.utils import BaseModel
from account.models import CustomUser
from product.models import ProductItem,Product

# Create your models here.

class Coupon(BaseModel):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code}: {self.discount}'


class Cart(BaseModel):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    discount = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    payable_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    def update_total(self):
        total = sum(item.total_price() for item in self.cart_items.all())
        self.total = total
        self.discount = self.coupon.discount if self.coupon else 0
        self.payable_amount = self.total - self.discount
        self.save()

    def save(self, *args, **kwargs):
        self.payable_amount = self.total - self.discount
        super().save(*args, **kwargs)

    def clean_cart(self):
        self.cart_items.all().delete()
        self.total = 0
        self.discount = 0
        self.payable_amount = 0
        self.coupon = None
        self.save()



class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_items')
    quantity = models.PositiveIntegerField(default=1)

    def unite_price(self):
        return self.product_item.price
    
    def total_price(self):
        return self.product_item.price * self.quantity

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.cart.update_total()
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.cart.update_total()


