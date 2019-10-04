from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_images, name='images'),
    url(r'^location/(\d+)', views.get_location, name='location'),
]