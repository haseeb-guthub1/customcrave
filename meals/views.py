from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredient, Recipe, MealPlan
from .serializers import IngredientSerializer, RecipeSerializer, MealPlanSerializer

@api_view(["GET", "POST"])
def ingredient_list(request):
    if request.method == "GET":
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def recipe_list(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def mealplan_list(request):
    if request.method == "GET":
        mealplans = MealPlan.objects.all()
        serializer = MealPlanSerializer(mealplans, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MealPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
