from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    share_price = models.PositiveIntegerField()
    market_cap = models.DecimalField(max_digits=15, decimal_places=2)
    source = models.URLField(blank=True)  # Assumes URLs for the source
    lot_size = models.PositiveIntegerField()
    min_qty = models.PositiveIntegerField()
    isin = models.CharField(max_length=20)
    special_comment = models.TextField(blank=True)
    sell_price_rupees = models.PositiveIntegerField(blank=True, null=True)
