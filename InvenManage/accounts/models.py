from django.db import models

# Create your models here.
class Registration(models.Model):
    userEmail = models.EmailField(max_length=255, unique=True, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255, null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    # Add Product Page
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    SKU = models.CharField(max_length=255, unique=True, null= True)
    product_name = models.CharField(max_length=255,null= True)
    category = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1200,null=True)
    price = models.CharField(max_length=255, null=True)
    sales_price = models.CharField(max_length=255,null= True)
    initial_quantity = models.CharField(max_length=255, null= True)
    low_stock_alert = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.description