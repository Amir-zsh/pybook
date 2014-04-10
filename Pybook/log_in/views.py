from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from accounts.models import UserProfile
from django.contrib.auth.models import User
# from django.template import RequestContext, loader

def log_in_view(request):
    return render(request,'log_in/login.html',)


def user_log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('main_site:wall', args=(username,)))
    else:
        return render(request, 'log_in/login.html', {'error_message': "username or password is invalid.",})
        
            
def user_sign_up(request):
    username=request.POST['new_username']
    password=request.POST['new_password']
    email=request.POST['email']
#     first_name=request.POST['first_name']
#     last_name=request.POST['last_name']
#     status=request.POST['satus']
#     birth_day=request.POST['birth_day']
    if not username or not email or not password:
        return render(request, 'log_in/login.html', {'error_message': "please complete required fields.",})
    
        
    try:
         user=User.objects.create_user(username=username, email=email, password=password)
    except:
         return render(request, 'log_in/login.html', {'error_message': "username is in use please try another.",})
    
    user.save()
    user_profile=UserProfile(user=user,)
    return HttpResponseRedirect(reverse('main_site:profiles', args=(username,)))

            