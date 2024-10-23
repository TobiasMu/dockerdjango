from django.db import models


# Create your models here.
class Trade(models.Model):
    counterparty = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id}, {self.product} , {self.quantity}, {self.price}"
