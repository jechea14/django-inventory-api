from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        
        # Specify Order of the fields
        fields = ('id', 'name', 'url')
        
class ProductSerializer(serializers.ModelSerializer):   
    
    # Show category name
    category = serializers.StringRelatedField(many=True) 
    
    class Meta:
        model = Product
        
        # Specify Order of the fields
        fields = ('id', 'name', 'price', 'qty', 'out_of_stock', 'category', 'first_created', 'last_updated')

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')
        
# class ProductSerializer(serializers.ModelSerializer):    
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'price', 'qty', 'out_of_stock', 'category', 'first_created', 'last_updated')