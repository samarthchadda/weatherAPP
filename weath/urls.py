from django.urls import path
from django.conf.urls import include, url
#importing all the views
from . import views


urlpatterns = [
    
    url('', views.index),
    
]
