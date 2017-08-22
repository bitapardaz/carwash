from django.db import models
from django.contrib.auth.models import User
from region_management.models import Region

# Create your models here.
class PromotionCode(models.Model):
    title = models.CharField(max_length=1000)
    code = models.CharField(max_length=100)
    valid_from = models.DateTimeField()
    expiry_date = models.DateTimeField()
    image = models.ImageField(upload_to='images')
    QR_code = models.ImageField(upload_to='images',null=True, blank=True)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title + "--" + self.title

class PromotionCodeRegion(models.Model):
    region = models.ForeignKey(Region)
    promotion_code = models.ForeignKey(PromotionCode)


class GiftCodeConsumption(models.Model):
    promotion_code = models.ForeignKey(PromotionCode)
    date_consumed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)


class ReferralGiftType(models.Model):
    title = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title


class ReferralGift(models.Model):
    gift_type = models.ForeignKey(ReferralGiftType)
    amount = models.IntegerField(default=0)
    valid_from = models.DateTimeField()
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    text_shown_to_customer_first_line = models.CharField(max_length=1000)
    text_shown_to_customer_second_line = models.CharField(max_length=1000)

class ReferralHistory(models.Model):
    referred = models.ForeignKey(User, related_name = 'source')
    new_commer = models.ForeignKey(User , related_name = 'destination')
    action_date = models.DateTimeField(auto_now=True)
    was_rewarded = models.BooleanField(default=False)
    reward = models.ForeignKey(ReferralGift,null=True,blank=True)
