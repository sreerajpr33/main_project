# Generated by Django 5.1.2 on 2024-12-11 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_brand_remove_product_size_remove_product_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
    ]