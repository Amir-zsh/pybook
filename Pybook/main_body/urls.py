from django.conf.urls import patterns,url
from main_body import views


urlpatterns = patterns('',
    url(r'^profile/$',views.profile_view, name='profile'),
    url(r'^messages/$',views.profile_view, name='Message'),
    url(r'^topics/$',views.profile_view, name='topics'),
    url(r'^news/$',views.profile_view, name='News'),
    url(r'^following/$',views.profile_view, name='following'),
    url(r'^(?P<user_name>.+)/wall/$', views.wall_view, name='Your_Wall'),
    url(r'^profileChange/$',views.profile_change_view, name='profile_Change'),
    url(r'^subchange/$',views.submit_changes, name='sub_Change'),
    url(r'^(?P<topic_sub>\w+)/$', views.topic_view, name='topic'),
    url(r'^(?P<topic_sub>.+)/post/$', views.send_post, name='post'),
    url(r'^(?P<topic_sub>.+)/like/$', views.like_post, name='like'),
    url(r'^search/$', views.search_users, name='search'),
    )