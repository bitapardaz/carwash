from rest_framework import serializers

from models import Service, ServiceType

class ServiceSerializer(serializers.ModelSerializer):

    #get_service_type = serializers.SerializerMethodField('get_service_type')

    def get_service_type(self,service):
        s_t = service.service_type
        s_t_s = ServiceTypeSerializer(st)
        return st.data

    class Meta:
        model = Service
        fields = ('service_type','car_type','price','duration','display_order',)

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id','title','confirmed','short_description','icon',
                  'image','movie_link','read_more', 'order')
