from rest_framework import serializers

from models import Config

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ('service_list','carwash_add_on_list','interconnection_time',
                  'slack_time','next_visit','inventory_item_processing_time',
                  'bad_customer_threshold','absence_threshold_days',
                  'is_service_type_dependency_updated',)
        
