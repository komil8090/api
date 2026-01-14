from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from .models import Product
from .serializers import ProductSerializer




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]





class ProductListByChildCategorySlugAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        slug = self.kwargs['slug']
        return Product.objects.filter(
            category__slug=slug,
            category__parent__isnull=False,
        
        ).select_related('category')



# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )

class Image(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/')
