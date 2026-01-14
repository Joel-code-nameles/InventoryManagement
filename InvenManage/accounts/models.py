from django.db import models

# Create your models here.
class Registration(models.Model):
    userEmail = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    conf_password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username