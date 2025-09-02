from rest_framework import serializers
from .models import Ingredient, Recipe, RecipeIngredient, MealPlan

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = "__all__"

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(source="recipeingredient_set", many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ["id", "title", "description", "category", "ingredients", "cooking_steps"]

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = "__all__"
