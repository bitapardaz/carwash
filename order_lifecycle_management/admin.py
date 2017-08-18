from django.contrib import admin

# Register your models here.
from models import OrderStatus, PaymentChannel, Order
from user_profile.models import UserProfile, CarWasherProfile
from django.core import urlresolvers



class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_order_details', 'date_created', 'get_customer_link','get_worker_link','get_status' , 'address', 'get_service_link', 'get_car_type', 'total_price', 'was_elibible_for_discount', 'alert', 'cancelled', 'changed')

    list_filter = ('alert','was_elibible_for_discount',)

    def get_order_details(self,obj):
        link=urlresolvers.reverse("admin:order_lifecycle_management_order_change", args=[obj.id])
        return u'<a href="%s"> details </a>' % (link)

    get_order_details.allow_tags = True

    def get_customer_link(self,obj):

        up = UserProfile.objects.get(user=obj.customer)

        #link=urlresolvers.reverse("admin:staff_time_management_timeslot_change", args=[obj.time_slot.id])
        link=urlresolvers.reverse("admin:user_profile_userprofile_change", args=[up.id])
        return u'<a href="%s"> %s </a>' % (link,up.mobile_number)

    get_customer_link.allow_tags = True

    def get_worker_link(self,obj):

        wp = UserProfile.objects.get(user=obj.worker)

        print wp.id

        #link=urlresolvers.reverse("admin:staff_time_management_timeslot_change", args=[obj.time_slot.id])
        link=urlresolvers.reverse("admin:user_profile_userprofile_change", args=[wp.id])
        return u'<a href="%s"> %s </a>' % (link,wp.mobile_number)

    get_worker_link.allow_tags = True


    def get_service_link(self,obj):
        return obj.service.service_type.title

    def get_car_type(self,obj):
        return obj.car_type.title

    def get_status(self,obj):
        return obj.status.title


admin.site.register(OrderStatus)
admin.site.register(PaymentChannel)
admin.site.register(Order,OrderAdmin)
