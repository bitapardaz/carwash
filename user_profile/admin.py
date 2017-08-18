from django.contrib import admin
import datetime
from datetime import timedelta
from system_config.models import Config

# Register your models here.
from models import UserProfile, Gender, KnownCar, KnownAdresses, MobileDevice, UserType, CarWasherProfile, SupervisorProfile, ConsumerProfile

class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)

class KnownCarAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user','get_user_type','mobile_number','rate','gender','number_of_cancellation' )
    list_filter = ('user_type__title',)


    def get_user(self,obj):
        return obj.user.username

    def get_user_type(self,obj):
        return obj.user_type.title

class MobileDeviceAdmin(admin.ModelAdmin):

    list_display = ('get_user','device_title','device_token','date')

    def get_user(self,obj):
        return obj.user.username


class ConsumerProfileAdmin(admin.ModelAdmin):

    list_display = ('get_user','balance','gift_balance', 'last_carwash_request', 'is_absent')
    list_filter = ('is_into_cars','likes_offroad',)

    def get_user(self,obj):
        return obj.user.username

    def is_absent(self,obj):
        absence_threshold_days = Config.objects.all()[0].absence_threshold_days
        last_order = obj.last_carwash_request
        last_order_naive = last_order.replace(tzinfo=None)
        now = datetime.datetime.now()
        actual_delta = now - last_order_naive

        accepted_delta = timedelta(days=absence_threshold_days)

        if actual_delta > accepted_delta :
            return u'<p>&#9746; <p>'
        else:
            return u'<p>&#9745; <p>'



    is_absent.allow_tags=True



admin.site.register(Gender,GenderAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(MobileDevice,MobileDeviceAdmin)
admin.site.register(UserType)


admin.site.register(ConsumerProfile,ConsumerProfileAdmin)

admin.site.register(KnownCar)
admin.site.register(KnownAdresses)

admin.site.register(CarWasherProfile)
admin.site.register(SupervisorProfile)
