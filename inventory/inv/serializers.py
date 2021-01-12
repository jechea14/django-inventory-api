from rest_framework import serializers
from .models import *

# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'url')
        
# class ProductSerializer(serializers.HyperlinkedModelSerializer):    
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'price', 'qty', 'out_of_stock', 'category', 'first_created', 'last_updated')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        
class ProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'qty', 'out_of_stock', 'category', 'first_created', 'last_updated')