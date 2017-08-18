from django.db import models
from django.contrib.auth.models import User
from car_information.models import Car
from region_management.models import Region

class Gender(models.Model):
    title = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title

#capturing roles such as Carwasher, Supervisor, Customer
# A user may have multiple roles.
class UserType(models.Model):

    title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    user_type = models.ForeignKey(UserType,null=True,blank=True)

    #security credentials
    token = models.CharField(max_length=100,null=True,blank=True)
    token_expiry = models.DateTimeField(null=True,blank=True)

    rate = models.IntegerField(default=10)
    mobile_number = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=100,null=True,blank=True)
    otp_expiration = models.DateTimeField(editable=True,null=True,blank=True)

    # additional information filled in by our staff. Used for promotions.
    gender = models.ForeignKey(Gender)
    age = models.IntegerField(default=0)

    number_of_cancellation = models.IntegerField(default=0)




    def __unicode__(self):
        return self.user.username

class ConsumerProfile(models.Model):
    user = models.ForeignKey(User)
    balance = models.IntegerField(default=0)
    gift_balance = models.IntegerField(default=0)
    is_into_cars = models.BooleanField(default=0)
    likes_offroad = models.BooleanField(default=0)
    last_carwash_request = models.DateTimeField()


class KnownCar(models.Model):
    user = models.ForeignKey(User)
    car = models.ForeignKey(Car)
    last_update = models.DateField()
    last_visit = models.DateField()
    # predict when the car needs car_wash again!
    next_visit_reminder = models.DateField()
    plate_number = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username + self.car.title


class KnownAdresses(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=200)
    date_verified = models.DateField()

    def __unicode__(self):
        return self.user.username + self.address


class MobileDevice(models.Model):
    user = models.ForeignKey(User)
    device_title = models.CharField(max_length=200)
    device_token = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.user.username + self.device_token


class CarWasherProfile(models.Model):
    user = models.ForeignKey(User,related_name = "main_user" )
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)

    national_number = models.CharField(max_length=12)
    id_scan_1 = models.ImageField(upload_to='images')
    id_scan_2 = models.ImageField(upload_to='images')
    id_scan_3 = models.ImageField(upload_to='images')

    # quantitative measures to evaluate carwasher
    total_time_available = models.IntegerField(default=0)
    total_orders_per_last_day = models.IntegerField(default=0)
    total_orders_current_week = models.IntegerField(default=0)
    total_orders_current_month = models.IntegerField(default=0)

    rate_of_cancellation = models.IntegerField(default=0)
    load = models.IntegerField(default=0) #percentage
    last_carwash_service = models.DateTimeField(null=True,blank=True)

    enabled = models.BooleanField(default=False)


class SupervisorProfile(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=100)
    #each supervisor has a number of regions under his/her authority
    regions = models.ManyToManyField(Region)
