from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from user_profile.models import KnownAdresses
from catalogue_management.models import Service
from car_information.models import CarType

class OrderStatus(models.Model):
    title = models.CharField(max_length=100)
    display_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class PaymentChannel(models.Model):
    title = models.CharField(max_length=100)
    display_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Order(models.Model):

    customer = models.ForeignKey(User, related_name = "customer")
    worker =  models.ForeignKey(User, related_name = "worker")
    date_created = models.DateTimeField(auto_now=True)

    #when registering an order, if the address does not exist before,
    #then first store it in the known addresses and then have the FK
    # here.
    address = models.ForeignKey(KnownAdresses)
    service = models.ForeignKey(Service)
    car_type = models.ForeignKey(CarType)
    comment = models.CharField(max_length=1000)

    original_price = models.IntegerField(default=0)
    was_elibible_for_discount = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    payment_channel = models.ForeignKey(PaymentChannel)
    payment_rrn = models.CharField(max_length=20)

    status = models.ForeignKey(OrderStatus)

    alert = models.BooleanField(default=False)

    worker_heads_off_at = models.DateTimeField(blank=True,null=True)
    worker_arrived_at = models.DateTimeField(blank=True,null=True)
    worker_finished_at = models.DateTimeField(blank=True,null=True)

    service_duration = models.IntegerField(default=0)
    cancelled = models.BooleanField(default=False)

    changed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.id)


#class OrderChangeLog():
#    order_id
