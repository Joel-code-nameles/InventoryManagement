from django.db import models

# Create your models here.
class Registration(models.Model):
    userEmail = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    # Add Product Page
    SKU = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    catergory = models.CharField(max_length=255)
    description = models.TextField(max_length=1200)
    price = models.CharField(max_length=255)
    sales_price = models.CharField(max_length=255)
    initial_quantity = models.CharField(max_length=255)
    low_stock_alert = models.CharField(max_length=255)

    def __str__(self):
        return self.description