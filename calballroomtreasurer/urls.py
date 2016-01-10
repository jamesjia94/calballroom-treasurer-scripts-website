from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import ipparser.views

urlpatterns = patterns('',
    url(r'^$', ipparser.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
