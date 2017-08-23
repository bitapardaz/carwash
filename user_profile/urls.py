from django.conf.urls import url
import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^signup/$',views.sign_up),
    url(r'^verify/$',views.verify),

]

urlpatterns = format_suffix_patterns(urlpatterns)
