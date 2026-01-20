from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('add_product/', views.add_product, name='add_product'),
    path('stock/', views.stock, name='stock'),
]