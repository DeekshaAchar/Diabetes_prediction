from django.db import models

# Create your models here.

class users(models.Model):
    name=models.CharField(max_length=50)

    ContactNumber=models.CharField(max_length=50)

    Email=models.CharField(max_length=50)

    Address=models.CharField(max_length=100)

    Username=models.CharField(max_length=50)

    Password=models.CharField(max_length=10)