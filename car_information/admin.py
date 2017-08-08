from django.contrib import admin

# Register your models here.

from models import Car,CarType

admin.site.register(Car)
admin.site.register(CarType)
