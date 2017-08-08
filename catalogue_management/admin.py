from django.contrib import admin

from models import ServiceType,Service,AddOnType,AddOn
# Register your models here.
admin.site.register(ServiceType)

admin.site.register(Service)
admin.site.register(AddOn)
admin.site.register(AddOnType)
