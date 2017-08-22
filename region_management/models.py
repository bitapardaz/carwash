from django.db import models

# Create your models here.
class Region(models.Model):
    title = models.CharField(max_length=200)
    display_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
