from . import models

from rest_framework import serializers


class MapSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Map
        fields = (
            'pk', 
            'LocName', 
        )


