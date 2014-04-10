from django.db import models
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
def wall_view(request):
    current_user=request.user
    if current_user.is_authenticated():
        return render(request, 'main/wall.html',{'user':current_user})
    else:
        return HttpResponseRedirect(reverse('index:login', ))
    
def profile_view(request):
    current_user=request.user
    if current_user.is_authenticated():
        return render(request, 'main/profile.html',{'user':current_user},)
    else:
        return HttpResponseRedirect(reverse('index:login', ))
def submit_chnages(requst):
    password=request.POST['new_password']
    email=request.POST['email']
    photo=request.POST['photo']
    statuse=request.POST['status']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    current_user.set_password(password)
    current_user=request.user
    if email:
        currnet_user.profile.email=email
    if photo:
        currnet_user.profile.photo=photo
    if first_name:
        currnet_user.profile.email=email
    
        
        
    
    
def topic_view():
    current_user=request.user
    if current_user.is_authenticated():
        return render(request, 'main/wall.html',{'user':current_user})
    else:
        return HttpResponseRedirect(reverse('index:login', ))
    pass


    
    