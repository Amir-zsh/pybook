from django.conf.urls import patterns,url
from main_body import views


urlpatterns = patterns('',
    url(r'^(?P<user_name>.+)/wall/$', views.wall_view, name='wall'),
    url(r'^(?P<user_name>\w+)/profile/$',views.profile_view, name='profile'),
    url(r'^(?P<user_name>\W+)/(\d+)/$', views.topic_view, name='topic'),
    url(r'^(?P<user_name>\W+)/(\d+)/$', views.search_view, name='search'),
    )
    
