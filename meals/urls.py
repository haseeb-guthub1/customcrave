from django.urls import path
from . import views

urlpatterns = [
    path("ingredients/", views.ingredient_list, name="ingredients"),
    path("recipes/", views.recipe_list, name="recipes"),
    path("mealplans/", views.mealplan_list, name="mealplans"),
]
