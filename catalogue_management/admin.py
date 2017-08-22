from django.contrib import admin

from models import ServiceType,Service,AddOnType,AddOn, AddonTypeServiceTypeDependency

class AddonTypeServiceTypeDependencyAdmin(admin.ModelAdmin):
    list_display = ('get_base','get_addon',)
    list_filter = ('base__title',)

    def get_base(self,obj):
        return obj.base.title

    def get_addon(self,obj):
        return obj.addon.title

admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(AddOn)
admin.site.register(AddOnType)
admin.site.register(AddonTypeServiceTypeDependency,AddonTypeServiceTypeDependencyAdmin)
