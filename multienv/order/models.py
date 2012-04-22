from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False