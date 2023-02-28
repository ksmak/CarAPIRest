# DRF
from rest_framework import serializers

# Local
from .models import (
    Car,
    Brand,
    Body,
    City,
    Engine
)


class CitySerializer(serializers.ModelSerializer):
    """Serializer for city."""
    class Meta:
        model = City
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    """Serializer for brand."""
    class Meta:
        model = Brand
        fields = "__all__"


class BodySerializer(serializers.ModelSerializer):
    """Serializer for body."""
    class Meta:
        model = Body
        fields = "__all__"


class EngineSerializer(serializers.ModelSerializer):
    """Serializer for generation."""
    class Meta:
        model = Engine
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    """Serializer for car."""
    city = CitySerializer()
    brand = BrandSerializer()
    body = BodySerializer()
    engine = EngineSerializer()

    class Meta:
        model = Car
        fields = "__all__"
