from django.contrib import admin

# Register your models here.
from models import PromotionCode,GiftCodeConsumption, ReferralHistory, ReferralGiftType, ReferralGift, ReferralHistory
from django.core import urlresolvers


class PromotionCodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'valid_from','expiry_date' , 'is_active',)
    list_filter = ('is_active',)

class GiftCodeConsumptionAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_promotion_title', 'get_promotion_code', 'date_consumed',)
    list_filter = ('promotion_code__code', 'promotion_code__code',)

    def get_user(self,obj):
        return obj.user.username


    def get_promotion_title(self,obj):
        link=urlresolvers.reverse("admin:promotions_promotioncode_change", args=[obj.promotion_code.id])
        #return u'<a href="%s">%s , %s , %s </a>' % (link,obj.time_slot.title, obj.time_slot.start_time, obj.time_slot.end_time)
        return u'<a href="%s"> %s </a>' % (link,obj.promotion_code.title)



    def get_promotion_code(self, obj):
        return obj.promotion_code.code

    get_promotion_title.allow_tags=True

class ReferralHistoryAdmin(admin.ModelAdmin):
    list_display = ('get_referred', 'get_new_commer','action_date')

    def get_referred(self,obj):
        return obj.referred.username

    def get_new_commer(self,obj):
        return obj.new_commer.username


class ReferralGiftAdmin(admin.ModelAdmin):
    list_display = ('get_gift_type', 'amount', 'valid_from', 'expiry_date', 'is_active')
    list_filter = ('is_active','gift_type__title')

    def get_gift_type(self,obj):
        return obj.gift_type.title


admin.site.register(PromotionCode,PromotionCodeAdmin)
admin.site.register(GiftCodeConsumption, GiftCodeConsumptionAdmin)
admin.site.register(ReferralGiftType)
admin.site.register(ReferralGift,ReferralGiftAdmin)
admin.site.register(ReferralHistory, ReferralHistoryAdmin)
