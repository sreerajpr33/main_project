# Generated by Django 5.1.2 on 2024-12-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_contact_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='address',
            field=models.TextField(default='phone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='phone',
            field=models.CharField(default='address', max_length=15),
            preserve_default=False,
        ),
    ]
