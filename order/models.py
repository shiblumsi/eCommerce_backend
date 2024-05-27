from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart, CartItem
from ecommerce_backend.utils import BaseModel
from product.models import ProductItem
User = get_user_model()


class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.user.email


class ShippingInfo(BaseModel):
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name+ ': ' + self.address.city


class PaymentMethod(BaseModel):
    payment_type = models.CharField(max_length=255)

    def __str__(self):
        return self.payment_type

class Order(models.Model):
    STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    shipping_info = models.ForeignKey(ShippingInfo, on_delete=models.CASCADE, default='')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)     #need to modifyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    discount = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    cart_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payable_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Processing')
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.payable_amount = self.cart_total + self.delivery_charge - self.discount
        super().save(*args, **kwargs)
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def total(self):
        return self.product_item.price * self.quantity

