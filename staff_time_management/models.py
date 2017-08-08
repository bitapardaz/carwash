from django.db import models
from django.contrib.auth.models import User
from customer_profile.models import Role
from system_config.models import AlertText


class TimeSlot(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    order = models.IntegerField(default=0)

class WorkerTimeTable(models.Model):
    user = models.ForeignKey(User)
    time_slot = models.ForeignKey(TimeSlot)
    activity_date = models.DateTimeField()
