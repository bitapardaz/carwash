from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=100)
    brand_logo = models.ImageField(upload_to='images')


class CarType(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title
