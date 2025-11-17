from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    cover_image = models.ImageField(upload_to="User Profiles",null=True,blank=True)

class BookDb(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    author = models.CharField(max_length=100,null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    publisher = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    cover_image = models.ImageField(upload_to="User Profiles",null=True,blank=True)