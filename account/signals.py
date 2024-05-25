from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser
from cart.models import Cart


@receiver(post_save, sender=CustomUser)
def create_cart(sender, instance, created, **kwargs):
    if created and instance.is_customer:
        Cart.objects.create(user=instance)
