from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Post.views.home', name='home'),
    url(r'^log_in/', include('log_in.urls',namespace='index')),
    url(r'^main/', include('log_in.urls',namespace='main')),

    url(r'^admin/', include(admin.site.urls)),
)
