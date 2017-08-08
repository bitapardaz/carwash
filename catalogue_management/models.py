from django.db import models

from car_information.models import CarType

class ServiceType(models.Model):
    title = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    read_more = models.CharField(max_length=1000,null=True,blank=True)

    def __unicode__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    service_type = models.ForeignKey(ServiceType)
    car_type = models.ForeignKey(CarType,null=True,blank=True)
    price = models.IntegerField(default=0)
    movie_link = models.CharField(max_length=1000,null=True,blank=True)

    duration = models.IntegerField(default=10) #minutes

    def __unicode__(self):
        return self.title

class AddOnType(models.Model):
    title = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images',null=True,blank=True)

    def __unicode__(self):
        return self.title


class AddOn(models.Model):
    addon_type = models.ForeignKey(AddOnType)
    read_more = models.CharField(max_length=1000,null=True,blank=True)
    price = models.CharField(max_length=100,default=0)
    car_type = models.ForeignKey(CarType)
    movie_link = models.CharField(max_length=1000,null=True,blank=True)
    duration = models.IntegerField(default=10) #minutes
