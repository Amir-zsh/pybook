from django.conf.urls import patterns, include, url
from log_in import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Post.views.home', name='home'),
    url(r'^log_in/', include('log_in.urls',namespace='index')),
    url(r'^main/', include('main_body.urls',namespace='main')),
    url(r'^log_out$', views.log_in_view, name='log_out'),

    url(r'^admin/', include(admin.site.urls)),
)
