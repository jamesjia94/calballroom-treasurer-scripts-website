from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import ipparser.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'calballroomtreasurer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ipparser.views.index, name='index'),
    url(r'^db', ipparser.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
