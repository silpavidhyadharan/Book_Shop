from django.db import models

# Create your models here.

class SignUpDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    confirm_password = models.CharField(max_length=100,null=True,blank=True)