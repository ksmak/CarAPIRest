# DRF
from rest_framework import viewsets

# Local
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """Viewset for task."""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
