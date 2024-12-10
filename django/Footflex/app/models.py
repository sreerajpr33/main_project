from django.db import models

# Create your models here.
class Product(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    stock=models.IntegerField()
    size=models.IntegerField()
    img=models.FileField()
    caregory=models.TextField()
    brand=models.TextField()

class Banner(models.Model):
    pic1=models.FileField()
    pic2=models.FileField()
    pic3=models.FileField()


