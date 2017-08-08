from django.db import models

from django.contrib.auth.models import User


class InventoryItemType(models.Model):
    item_type = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)

# Create your models here.
class InventoryItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    #unique code to track the asset
    tracking_code = models.CharField(max_length=100)
    item_type= models.ForeignKey(InventoryItemType,null=True,blank=True)

    is_available = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class InventoryDeliveryStatus(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class InventoryRequest(models.Model):

    user = models.ForeignKey(User)
    item = models.ForeignKey(InventoryItem)
    quantity = models.IntegerField(default=0)
    request_time = models.DateTimeField(editable=True)

    delivery_time = models.DateTimeField(editable=True)
    delivery_location = models.CharField(max_length=1000,null=True,blank=True)
    status = models.ForeignKey(InventoryDeliveryStatus)
    comments = models.CharField(max_length=1000)

    # if the request is not processed within 10 minutes.
    alarm_raised = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username + "-" + self.item.title
