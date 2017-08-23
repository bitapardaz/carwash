from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^get_system_config/$',views.get_system_config),
]

urlpatterns = format_suffix_patterns(urlpatterns)
