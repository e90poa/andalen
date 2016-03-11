from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views import generic

# from andalen.apps import tasks
#from .views import index
import views

urlpatterns = patterns("",

    url(r'^$', views.index, name='index'),

)
