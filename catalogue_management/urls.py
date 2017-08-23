from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^get_service_types/$',views.get_service_types),
    url(r'^get_services/$',views.get_services),

]

urlpatterns = format_suffix_patterns(urlpatterns)
