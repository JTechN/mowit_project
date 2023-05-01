from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from django.db.models import Q, F



class Tag(models.Model):
  name = models.CharField(max_length=200, null=True)
  def __str__(self):
    return self.name

class Service(models.Model):

  account = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  name = models.CharField(max_length=200, null=True)
  price = models.FloatField(null=True)
  description = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.name

class OrderStatus(models.Model):
  STATUS = (
    ('Pending', 'Pending'),
    ('Out for Service', 'Out for Service'),
    ('Completed', 'Completed'),
  )
  # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
  service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  status = models.CharField(max_length=200, null=True, choices=STATUS)


  STATUS_FIELD = 'status'



#Rating System for Contractor

#User Profile

class RequestService(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer', default=1)
    contractor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contractor', default=1)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_request = models.DateTimeField(auto_now_add=True)
    Status = 'Pending'
