from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PriceHistory
from .serializers import PriceHistorySerializer

@api_view(["GET", "POST"])
def pricehistory_list(request):
    if request.method == "GET":
        prices = PriceHistory.objects.all()
        serializer = PriceHistorySerializer(prices, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PriceHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
