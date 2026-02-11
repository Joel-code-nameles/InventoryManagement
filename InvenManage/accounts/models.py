from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    SKU = models.CharField(max_length=255, unique=True, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=1200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    initial_quantity = models.IntegerField(null=True, blank=True, default=0)
    low_stock_alert = models.IntegerField(null=True, blank=True, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name or f"Product {self.id}"
    