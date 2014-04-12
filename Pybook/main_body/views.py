from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# @login_required
def wall_view(request):
    current_user=request.user
    if current_user.is_authenticated():
        return render(request, 'main/wall.html',{'user':current_user})
    else:
        return HttpResponseRedirect(reverse('index:login', ))
@login_required
def topic_view(request,user_name,topic_id):
    topic=Topic.set_all.get(pk=topic_id)
    current_user=request.user
    if current_user.is_authenticated():
        return render(request, 'main/topic.html',{'user':current_user,'topic':topic},)
    else:
        return HttpResponseRedirect(reverse('index:login', ))  
def profile_view(request,user_name):
    owner=get_object_or_404(User,username=user_name)
    current_user=request.user
    if current_user.is_authenticated() and current_user==owner :
        return render(request, 'main_body/Profile.html',{'user':current_user},)
    else:
        return HttpResponseRedirect(reverse('index:login', ))
def message_view(reques,user_name):
    owner=get_object_or_404(User,username=user_name)
    current_user=request.user
    if current_user.is_authenticated() and current_user==owner :
        return render(request, 'main/messages.html',{'user':current_user},)
    else:
        return HttpResponseRedirect(reverse('index:login', ))

def submit_chnages(requst):
    password=request.POST['new_password']
    email=request.POST['email']
    photo=request.POST['photo']
    statuse=request.POST['status']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    if password:
        current_user.set_password(password)
    current_user=request.user
    user_profile=UserProfile(user=current_user,)
    user_profile.save()
    if email:
        currnet_user.profile.email=email
    if photo:
        currnet_user.profile.photo=photo
    if first_name:
        currnet_user.profile.email=email
    if last_name:
        current_user.profile.last_name=last_name
    return render(request,'main/profile.html',{'user':current_user})
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('log_out',))


    
    