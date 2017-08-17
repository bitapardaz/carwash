from django.contrib import admin

from models import TimeSlot, WorkerTimeTable
from django.core import urlresolvers

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time', 'order')

class WorderTimeTableAdmin(admin.ModelAdmin):
    list_display = ('user','day', 'hour_start', 'hour_end', 'link_to_time_slot' , 'activity_date' , 'region')

    def link_to_time_slot(self,obj):
        link=urlresolvers.reverse("admin:staff_time_management_timeslot_change", args=[obj.time_slot.id])
        #return u'<a href="%s">%s , %s , %s </a>' % (link,obj.time_slot.title, obj.time_slot.start_time, obj.time_slot.end_time)
        return u'<a href="%s"> Go </a>' % (link)

    def day(self,obj):
        return obj.time_slot.day

    def hour_start(self,obj):
        return obj.time_slot.start_time

    def hour_end(self,obj):
        return obj.time_slot.end_time

    link_to_time_slot.allow_tags=True


admin.site.register(TimeSlot,TimeSlotAdmin)
admin.site.register(WorkerTimeTable,WorderTimeTableAdmin)
