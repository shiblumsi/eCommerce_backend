# Generated by Django 5.0.4 on 2024-05-09 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.brand'),
        ),
    ]
