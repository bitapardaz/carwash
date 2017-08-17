from django.db import models

class CarType(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,null=True,blank=True)
    car_type = models.ForeignKey(CarType,null=True,blank=True)
    brand_logo = models.ImageField(upload_to='images')
