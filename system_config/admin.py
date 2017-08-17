from django.contrib import admin

# Register your models here.
from models import Config,AlertText


admin.site.register(Config)
admin.site.register(AlertText)
