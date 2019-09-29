from . import models
from . import serializers
from rest_framework import viewsets, permissions


class MapViewSet(viewsets.ModelViewSet):
    """ViewSet for the Map class"""

    queryset = models.Map.objects.all()
    serializer_class = serializers.MapSerializer
    permission_classes = [permissions.IsAuthenticated]


