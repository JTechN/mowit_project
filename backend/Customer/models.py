from django.db import models

# Create your models here.

class Customer(models.Model):
  customer_name = models.CharField(max_length=100)
  customer_email = models.CharField(max_length=100)
  customer_phone = models.CharField(max_length=10)
  customer_address = models.CharField(max_length=100)
  customer_zipcode = models.CharField(max_length=10)
