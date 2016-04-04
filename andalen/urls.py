from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views import generic

from andalen.apps import tasks

admin.autodiscover()


urlpatterns = patterns("",

    # Admin URLs.
    url(r"^admin/", include(admin.site.urls)),

    url(r"^api/", include(tasks.api.urls)),
    url(r"^tasks/", include(tasks.urls)),

    
    # Mount all the urls defined in tasks.urls
    #url(r"^tasks/", include(tasks.urls)),

    # There's no favicon here!
    url(r"^favicon.ico$", generic.RedirectView.as_view()),
    
)
