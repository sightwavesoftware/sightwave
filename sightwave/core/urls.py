from django.conf.urls import url
from sightwave.core import views


urlpatterns = [
    url(r'^', views.home, name='core'),
]
