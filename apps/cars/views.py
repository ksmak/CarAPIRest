# DRF
from rest_framework import viewsets

# Local
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    """Viewset for car."""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
