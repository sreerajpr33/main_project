from django.db import models

class Brand(models.Model):
    name=models.TextField()

class Category(models.Model):
    c_name=models.TextField()


# Create your models here.
class Product(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.TextField()

class Banner(models.Model):
    pic1=models.FileField()
    pic2=models.FileField()
    pic3=models.FileField()

class Banner2(models.Model):
    pic1=models.FileField()
    pic2=models.FileField()
    b_name=models.TextField()
    b_dis=models.TextField()

class Size(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.IntegerField()
    stock=models.IntegerField()


