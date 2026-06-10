from django.db import models
from SalesBill.models import *


# Create your models here.
class PaymentMaster(models.Model):
    sale = models.ForeignKey(SalesBill, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=50)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    payment_date = models.DateField()
    remarks = models.TextField(null=True, blank=True)


class ReturnRefund(models.Model):
    sale = models.ForeignKey(SalesBill, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    refund_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class StockTransaction(models.Model):
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)