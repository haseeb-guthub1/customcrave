from django.db import models

# Create your models here.
from django.db import models
from meals.models import Ingredient

class PriceHistory(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store_name = models.CharField(max_length=100)
    store_url = models.URLField()
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ingredient.name} - {self.price} ({self.store_name})"
