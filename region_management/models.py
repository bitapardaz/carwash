from django.db import models

# Create your models here.
class Region(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    #other region attributes
