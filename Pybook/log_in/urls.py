from django.conf.urls import patterns,url


from log_in import views

urlpatterns = patterns('',
    url(r'^$', views.log_in_view, name='login'),
    url(r'^log_in$', views.user_log_in, name='log_in'),
    url(r'^sign_up$', views.user_sign_up, name='sign_up'),
    url(r'^log_out$', views.log_in_view, name='log_out'),
    
    
)
    