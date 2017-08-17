from django.contrib import admin

# Register your models here.

from models import Car,CarType

class CarAdmin(admin.ModelAdmin):

    list_display = ('title','brand_logo','subtitle','get_car_type', )
    list_filter = ('car_type__title',)
    def get_car_type(self,obj):
        return obj.car_type.title



admin.site.register(Car, CarAdmin)
admin.site.register(CarType)
