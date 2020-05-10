from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    stock = models.IntegerField()
    price = models.FloatField()

class Order(models.Model):
    order_date = models.DateField()
    quantity = models.IntegerField()
    total = models.FloatField()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null= True, on_delete=models.SET_NULL, related_name='items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    total = models.FloatField()

