from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from client.models import Client
from bankModel.models import Bank

from .serializer import ClientSerializer
from .serializer import BankAccountSerializer


class ClientListView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BankAccountListView(APIView):
    def get(self, request):
        bank = Bank.objects.all()
        serializer = BankAccountSerializer(bank, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BankAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
