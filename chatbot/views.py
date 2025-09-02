from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ChatHistory
from .serializers import ChatHistorySerializer

@api_view(["GET", "POST"])
def chat_list(request):
    if request.method == "GET":
        chats = ChatHistory.objects.all()
        serializer = ChatHistorySerializer(chats, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ChatHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Here you can later integrate actual chatbot NLP response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
