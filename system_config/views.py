from django.shortcuts import render

from models import Config
from serializers import ConfigSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_system_config(request):
    config = Config.objects.all()[0]
    serializer = ConfigSerializer(config)
    return Response(serializer.data)
