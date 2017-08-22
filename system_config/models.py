from django.db import models

# Create your models here.

#describes which bits of information on the client
#need to be updated when the app is started.
class Config(models.Model):
    service_list = models.BooleanField(default=False)
    carwash_add_on_list = models.BooleanField(default=False)

    #time that takes the carwash person to move from his current
    #location to the next location.
    interconnection_time = models.IntegerField(default=20)

    #the closest time that a customer can submit an order for.
    slack_time = models.IntegerField(default=10)

    # next visit (customer_profile.known_cars)
    next_visit = models.IntegerField(default=10)

    # time it takes for the InventoryItemRequest to be processed.
    inventory_item_processing_time = models.IntegerField(default=10)

    # Threshold above which the customer is deemed to be a bad
    # customer in the sense that she cancells the orders too
    # frequently
    # see customer_profile.number_of_cancellation
    # at the end of every month, this gets reset
    bad_customer_threshold = models.IntegerField(default=4)

    # absence threshold for the ConsumerProfile
    absence_threshold_days = models.IntegerField(default=10)

#    def __unicode__(self):
#        return self.service_list
    is_service_type_dependency_updated = models.BooleanField(default=False)

class AlertText(models.Model):
    title = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.service_list
