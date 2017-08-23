from rest_framework import serializers

from models import CarType


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ('title','confirmed','icon')
