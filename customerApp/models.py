from django.db import models

# Create your models here.
class CustomerMaster(models.Model):
    customer_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
  
    is_active = models.BooleanField(default=True)