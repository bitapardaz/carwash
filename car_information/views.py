from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from models import CarType
from serializers import CarTypeSerializer

@api_view(['GET'])
def get_car_types(request):
    output = {}
    car_types = CarType.objects.all()
    serializer = CarTypeSerializer(car_types,many=True)
    return Response(serializer.data)
