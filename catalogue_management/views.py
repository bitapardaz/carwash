from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import ServiceSerializer, ServiceTypeSerializer

from car_information.models import CarType
from models import ServiceType,Service

# Create your views here.
@api_view(['GET'])
def get_services(request):
    services = Service.objects.all( )
    serializer = ServiceSerializer(services,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_service_types(request):
    service_types = ServiceType.objects.all()
    serializer = ServiceTypeSerializer(service_types,many=True)
    return Response(serializer.data)
