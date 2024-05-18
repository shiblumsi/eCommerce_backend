from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE, related_name='categories',null=True,blank=True)
    image = models.ImageField(upload_to='images/category')

    def __str__(self):
        return self.name
    


class Brand(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Color(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Size(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='products',null=True,blank=True)

    def __str__(self):
        return self.name
    
    


class ProductItem(BaseModel):
    AVAILABILITY = (
        ('Available', 'Available'),
        ('Out of Stock', 'Out of Stock'),
    )

    stock_available = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20, choices=AVAILABILITY, default='Available')
    is_active = models.BooleanField(default=True)

    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product_items')
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        product_name = self.product.name if self.product else "Unknown Product"
        color_name = self.color.name if self.color else "Unknown Color"
        size_name = self.size.name if self.size else "Unknown Size"
        return f'{product_name}, {color_name}, {size_name}'
    


class ProductImage(BaseModel):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/productItem')

