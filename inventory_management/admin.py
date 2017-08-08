from django.contrib import admin

# Register your models here.
from models import InventoryItem,InventoryRequest,InventoryDeliveryStatus

admin.site.register(InventoryItem)
admin.site.register(InventoryRequest)
admin.site.register(InventoryDeliveryStatus)
