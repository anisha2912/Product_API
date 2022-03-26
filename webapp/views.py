import imp
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Products
from . serializers import ProductsSerializer

# Create your views here.
class Productslist(APIView):

    def get(self, request):
        Product1= Products.objects.all()
        serializer=ProductsSerializer(Product1, many=True)
        return Response(serializer.data)

    def post(self):
        pass