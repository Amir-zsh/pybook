from django.conf.urls import patterns,url


from log_in import views

urlpatterns = patterns('',
    url(r'^(?p<user_name>.+)/wall$', views.log_in_view, name='wall'),
    url(r'^(?p<user_name>.+)/profile$', views.user_log_in, name='profile'),
    url(r'^(?p<user_name>.+)/(?p<topic_name>.+)', views.topic_view, name='topic')
    
    
    )
    