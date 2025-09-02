from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=50, default="g")  # e.g., grams, ml
    latest_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    store_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("snack", "Snack"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    cooking_steps = models.TextField()

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Quantity in given unit")

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity} {self.ingredient.unit}"


class MealPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MealPlan ({self.user.username}) - {self.created_at.date()}"
