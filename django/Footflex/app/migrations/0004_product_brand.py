# Generated by Django 5.1.2 on 2024-12-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]
