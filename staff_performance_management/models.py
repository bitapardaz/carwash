from django.db import models
from django.contrib.auth.models import User
from customer_profile.models import Role
from system_config.models import AlertText


'''
class WorkerAlert(models.Model)
    user = models.ForeignKey(User)
    alert_cause = models.ForeignKey(AlertText)
    alert_time = models.DateTimeField()
    #order_id
    alert_seen = models.BooleanField(defulat=False)
    escalate_alert_to_manager = models.BooleanField(default=False)

class RatePerCarType(models.Model):
    worker = models.ForeignKey(Worker)
    service = models.ForeignKey(Service)
    rate = models.IntegerField(default=0)

class WorkerPerformance(models.Model):
    worker = models.ForeignKey(Worker)
    service = models.ForeignKey(Service)
    car_type = models.ForeignKey(CarType)
    duration = models.IntegerField(default=0)

    calculate being late using the order start_time

class WorkerReport(models.Model):
    start_time = models.DateField(null=True,blank=True)
    number_of_orders = models.IntegerField(default=0)
    penalty = models.IntegerField(default=0)


class WorkerLocationLog(models.Model):


'''
