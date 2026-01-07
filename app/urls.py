from django.urls import path, include
from django.contrib import admin
from .views import (
    car_list_create,
    car_detail,
    CarListCreateAPIView,
    CarRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),
]


urlpatterns = [
    # FBV
    path('fbv/cars/', car_list_create),
    path('fbv/cars/<int:pk>/', car_detail),

    # CBV
    path('cbv/cars/', CarListCreateAPIView.as_view()),
    path('cbv/cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view()),
]
