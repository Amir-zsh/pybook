from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from accounts.models import UserProfile
from django.contrib.auth.models import User
from mail_validity import valid_mail
# from django.template import RequestContext, loader

def log_in_view(request):
    context = {}
    return render(request,'log_in/login.html',context)


def user_log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('main:profile', args=(username,)))
    else:
        return render(request, 'log_in/login.html', {'error_message': "username or password is invalid.",})
        
            
def user_sign_up(request):
    user_name=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    gender=request.POST['Gender']
    if not user_name or not email or not password:
        return render(request, 'log_in/login.html', {'error_message': "please complete required fields.",})

    if email:
        if vali_mail(email)==False:
            return render(request, 'log_in/login.html', {'error_message': "please enter a valid mail(Only letters, numbers, underscores, and one dot (.) are allowed)",})
    
        
    try:
         user=User.objects.create_user(username=user_name, email=email, password=password)
    except:
         return render(request, 'log_in/login.html', {'error_message': "username is in use please try another.",})
    
    user.save()
    user = authenticate(username=user_name, password=password)
    login(request,user)
    profile=UserProfile(user=user)
    profile.save()
    
    return HttpResponseRedirect(reverse('main:profile',))
    
    
    
    

            
