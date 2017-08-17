from django.db import models
from django.contrib.auth.models import User
from system_config.models import AlertText
from region_management.models import Region

class TimeSlot(models.Model):
    day = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return  self.start_time + " -- " + self.end_time + " -- " + self.day



class WorkerTimeTable(models.Model):
    user = models.ForeignKey(User)
    time_slot = models.ForeignKey(TimeSlot)
    activity_date = models.DateTimeField()
    region = models.ForeignKey(Region,null=True,blank=True)
