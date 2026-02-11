from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('SKU', 'product_name', 'category', 'price', 'initial_quantity')
    search_fields = ('product_name', 'SKU', 'category')
    list_filter = ('category',)

# Register the Product model with custom admin options
admin.site.register(Product, ProductAdmin)
