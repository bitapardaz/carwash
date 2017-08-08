from django.contrib import admin

# Register your models here.
from models import OrderStatus, PaymentChannel, Order
admin.site.register(OrderStatus)
admin.site.register(PaymentChannel)
admin.site.register(Order)
