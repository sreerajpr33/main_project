# Generated by Django 5.1.2 on 2024-12-11 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_caregory_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='c_name',
        ),
    ]
