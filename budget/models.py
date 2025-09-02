from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Budget(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    daily_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    weekly_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Budget"


class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    meal_plan = models.ForeignKey("meals.MealPlan", on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Expense {self.cost} for {self.budget.user.username}"
