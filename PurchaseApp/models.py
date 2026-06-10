from django.db import models
from suplierApp.models import *
from PurchaseApp.models import *
from productApp.models import *
from authApp.models import*


# Create your models here.
class PurchaseEntry(models.Model):
    supplier = models.ForeignKey(SupplierMaster, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_date = models.DateField()
    invoice_no = models.CharField(max_length=100, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(PurchaseEntry, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)