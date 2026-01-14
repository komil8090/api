from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsEditableWithin4Hours


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer

    def get_permissions(self):
        """
        GET → hamma kora oladi
        POST/PUT/PATCH/DELETE → 4 soatlik cheklov
        """
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsEditableWithin4Hours()]


