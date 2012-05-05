from django.db import models

from core.models import Environment

class Order(Environment):
    order_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
