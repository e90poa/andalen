from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views import generic

# from andalen.apps import tasks
#from .views import index
import resources

urlpatterns = patterns("",
	url(r'^tasks/$', resources.TaskList.as_view(), name='task-list'),
	url(r'^tasks/(?P<pk>\d+)$', resources.TaskDetail.as_view(), name='task-detail'),
)
