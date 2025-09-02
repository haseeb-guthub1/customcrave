from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Extend default user
    diet_type = models.CharField(
        max_length=50,
        choices=[
            ("vegetarian", "Vegetarian"),
            ("non-vegetarian", "Non-Vegetarian"),
            ("vegan", "Vegan"),
            ("keto", "Keto"),
            ("custom", "Custom"),
        ],
        default="non-vegetarian"
    )
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.username
