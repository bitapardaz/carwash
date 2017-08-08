from django.contrib import admin

# Register your models here.
from models import CustomerProfile, Gender, KnownCar, KnownAdresses, MobileDevice, UserType, Role

admin.site.register(CustomerProfile)
admin.site.register(Gender)
admin.site.register(KnownCar)
admin.site.register(KnownAdresses)
admin.site.register(MobileDevice)
admin.site.register(UserType)
admin.site.register(Role)
