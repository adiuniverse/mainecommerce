from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    


class Seller(models.Model):
    seller_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.BigIntegerField()
    company_name = models.CharField(max_length = 50)
    accountholder_name = models.CharField(max_length = 20)
    ifsc = models.BigIntegerField()
    branch = models.CharField(max_length = 25)
    account_number = models.BigIntegerField()
    password = models.CharField(max_length = 20)
    seller_pic = models.ImageField(upload_to='seller/', default="")
    user_name = models.CharField(max_length = 20 , default="")


