from django.db import models

# Create your models here.
class Registration(models.Model):
    CompanyName = models.CharField(max_length=255)
