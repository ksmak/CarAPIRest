# DRF
from rest_framework import serializers

# Local
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for task."""
    class Meta:
        model = Task
        fields = "__all__"