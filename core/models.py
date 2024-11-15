from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=50)

    class ProductClass(models.TextChoices):
        Bond = "Bond", "Bond"
        Equity = "Equity", "Equity"
        Interst = "Interst", "Interest"
        Forex = "Forex", "Forex"
        Commodities = "Commodities", "Commodities"

    class ProductType(models.TextChoices):
        Option = "Option", "Option"
        Forward = "Forward", "Forward"
        Future = "Future", "Future"
        Swap = "Swap", "Swap"
        SwapCrossCurrency = "SwapCrossCurrency", "SwapCrossCurrency"
        Spot = "Spot", "Spot"
        Standard = "Standard", "Standard"

    product_type = models.CharField(
        max_length=20, choices=ProductType.choices, default=ProductType.Standard
    )

    product_class = models.CharField(
        max_length=20, choices=ProductClass.choices, default=ProductClass.Bond
    )

    def __str__(self):
        return (
            f"{self.id}, {self.product_type} , {self.product_class}, {self.description}"
        )


class CounterParty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class TradingBook(models.Model):
    name = models.CharField(max_length=50, default="book")

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class Trade(models.Model):
    counterparty = models.ForeignKey(CounterParty, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tradingbook = models.ForeignKey(TradingBook, on_delete=models.CASCADE)

    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id}, {self.product} , {self.quantity}, {self.price}"
