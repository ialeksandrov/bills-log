# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bills(models.Model):
    bill_name = models.CharField(max_length=200)
    bill_month = models.CharField(max_length=50)
    bill_amount = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self):
        return self.bill_name
