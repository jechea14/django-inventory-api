from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

# Serializer version, does all the CRUD

# class CategoryView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# class ProductView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Products': '/product/',
        'Product-Detail': '/product/<id>',
        'Product-Create': '/product-create/',
        'Product-Update': '/product-update/<id>',
        'Product-Delete': '/product-delete/<id>',
        'Category': '/category/',
        'Category-Detail': '/category/<id>',
        'Category-Create': '/category-create/',
        'Category-Update': '/category-update/<id>',
        'Category-Delete': '/category-delete/<id>',
    }   
    return Response(api_urls)

# Product CRUD
@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()   
    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()   
    return Response('Product Successfully Deleted.')

# Category CRUD
@api_view(['GET'])
def categoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categoryDetail(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def categoryCreate(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
    return Response(serializer.data)

@api_view(['POST'])
def categoryUpdate(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()   
    return Response(serializer.data)

@api_view(['DELETE'])
def categoryDelete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()   
    return Response('Category Successfully Deleted.')