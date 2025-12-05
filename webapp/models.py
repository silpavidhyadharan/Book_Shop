from django.db import models

# Create your models here.

class SignUpDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    confirm_password = models.CharField(max_length=100,null=True,blank=True)

class ContactDb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    bookname = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    total_price = models.IntegerField(null=True,blank=True)
    book_image = models.ImageField(upload_to="Cart Images",null=True,blank=True)

