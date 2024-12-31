from django.http import HttpResponse
from django.shortcuts import render
from api.models import Category, Product
from api.serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

def home(request):
    return HttpResponse("Hello")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=["get"], detail=True, name="Products by category")
    def products(self, request, pk=None):
        category = self.get_object()
        product_serializer = ProductSerializer(
            category.products, many=True, context={"request": request}
        )
        return Response(product_serializer.data)