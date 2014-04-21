from django.conf.urls import patterns,url
from main_body import views


urlpatterns = patterns('',
    url(r'^profile/$',views.profile_view, name='profile'),
    url(r'^messages/$',views.profile_view, name='Message'),
    url(r'^following/$',views.profile_view, name='following'),
    url(r'^(?P<user_name>.+)/wall/$', views.wall_view, name='Your_Wall'),
    url(r'^profileChange/$',views.profile_change_view, name='profile_Change'),
    url(r'^subchange/$',views.submit_changes, name='sub_Change'),
    url(r'^topics/$', views.topics_list_view, name='topics'),
    url(r'^topics/(?P<topic_sub>\w+)/$', views.topic_view, name='topic'),
    url(r'^(?P<topic_id>\d+)/post/$', views.send_post, name='send_post'),
    url(r'^(?P<post_id>\d+)/comment/$', views.send_comment, name='comment'),
    url(r'^(?P<post_id>\d+)/like/$', views.like_post, name='like'),
    url(r'^(?P<post_id>\d+)/like/$', views.unlike_post, name='unlike'),
    url(r'^search-result/$', views.search_users, name='search'),
    url(r'^(?P<user_name>.+)/follow$', views.follow_user, name='follow'),
    url(r'^news/$', views.news_view, name='News'),
    
    
    )