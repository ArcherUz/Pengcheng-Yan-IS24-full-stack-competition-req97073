from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer
# Create your views here.

class HealthCheckView(generics.GenericAPIView):
    def get(self, request):
        return JsonResponse({'status': 'healthy'})

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer