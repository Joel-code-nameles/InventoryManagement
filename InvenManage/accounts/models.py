from django.db import models

# Create your models here.
class Registration(models.Model):
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    conf_password = models.CharField(max_length=255)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username