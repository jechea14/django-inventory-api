from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.PositiveIntegerField()
    out_of_stock = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    first_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name