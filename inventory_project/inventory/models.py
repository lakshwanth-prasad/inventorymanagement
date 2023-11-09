from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=255)

class Product(models.Model):
    product_id = models.CharField(max_length=100,primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    stock_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    