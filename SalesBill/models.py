from django.db import models
from customerApp.models import *
from productApp.models import *

# Create your models here.
class SalesBill(models.Model):
    customer = models.ForeignKey(CustomerMaster, on_delete=models.SET_NULL, null=True, blank=True)
    bill_no = models.CharField(max_length=100, unique=True)
    bill_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payable_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=30, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)


class SalesItem(models.Model):
    sale = models.ForeignKey(SalesBill, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)