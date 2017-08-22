from django.db import models

from car_information.models import CarType

class ServiceType(models.Model):
    title = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    short_description = models.CharField(max_length=100,blank=True,null=True)
    icon = models.ImageField(upload_to='images',null=True,blank=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    movie_link = models.CharField(max_length=1000,null=True,blank=True)
    read_more = models.CharField(max_length=1000,null=True,blank=True)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Service(models.Model):
    service_type = models.ForeignKey(ServiceType)
    car_type = models.ForeignKey(CarType,null=True,blank=True)
    price = models.IntegerField(default=0)
    display_order = models.IntegerField(default=0)

    duration = models.IntegerField(default=10) #minuteso

    def __unicode__(self):
        return self.service_type.title + "-" + self.car_type.title

class AddOnType(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    confirmed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    movie_link = models.CharField(max_length=1000,null=True,blank=True)
    read_more = models.CharField(max_length=1000,null=True,blank=True)
    short_description = models.CharField(max_length=1000,null=True,blank=True)

    def __unicode__(self):
        if self.title == None:
            return "empty"
        else:
            return self.title


class AddOn(models.Model):
    addon_type = models.ForeignKey(AddOnType)
    read_more = models.CharField(max_length=1000,null=True,blank=True)
    price = models.CharField(max_length=100,default=0)
    car_type = models.ForeignKey(CarType)
    duration = models.IntegerField(default=10) #minutes
    short_description = models.CharField(max_length=1000,null=True,blank=True)

    def __unicode__(self):
        return self.addon_type.title + "--" + self.car_type.title

# each service type can allow a number of addons.
class AddonTypeServiceTypeDependency(models.Model):
    base = models.ForeignKey(ServiceType)
    addon = models.ForeignKey(AddOnType)
