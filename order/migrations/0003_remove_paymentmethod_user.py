# Generated by Django 5.0.4 on 2024-05-27 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_address_order_is_paid_shippinginfo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='user',
        ),
    ]