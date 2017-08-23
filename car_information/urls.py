from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^get_car_types/$',views.get_car_types),
]

urlpatterns = format_suffix_patterns(urlpatterns)
