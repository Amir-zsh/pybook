from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile 
from main_body.models import *

import datetime

@login_required
def wall_view(request,user_name):
    current_user=request.user
    posts=Post.objects.filter(author=current_user)
    return render(request, 'main_body/Wall.html',{'user':current_user,'posts':posts})
@login_required
def topic_view(request,topic_sub):
    topic=Topic.objects.get(subject=topic_sub)
    current_user=request.user
    if current_user.is_authenticated():
        return render(request, 'main_body/Topic.html',{'user':current_user,'topic':topic},)
    else:
        return HttpResponseRedirect(reverse('index:login', ))
@login_required 
def profile_view(request):
    current_user=request.user
    birth=current_user.profile.birth_day
    if birth:
        birth_day=str(birth.year)+"/"+str(birth.month)+"/"+str(birth.day)
    else:
        birth_day=None
    return render(request, 'main_body/Profile.html',{'user':current_user,"birth_day":birth_day},)
@login_required
def profile_change_view(request):
    current_user=request.user
    return render(request, 'main_body/Profile(Change).html',{'user':current_user},)
    
def message_view(reques):
    owner=get_object_or_404(User,username=user_name)
    current_user=request.user
    if current_user.is_authenticated() and current_user==owner :
        return render(request, 'main/messages.html',{'user':current_user},)
    else:
        return HttpResponseRedirect(reverse('index:login', ))

def submit_changes(request):
    password=request.POST['new_password']
    email=request.POST['email']
    photo=request.POST.get('photo',False)
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    month=int(request.POST['Month'])
    print(month)
    year=int(request.POST['Year'])
    day=int(request.POST['Day'])
    country=request.POST['Country']
    current_user=request.user
    if password:
        current_user.set_password(password)
    if email:
        current_user.email=email
    if photo:
        current_user.profile.photo=photo
    if first_name:
        current_user.profile.first_name=first_name
    if last_name:
        current_user.profile.last_name=last_name
    if country:
        current_user.profile.country=country
    if day and month and year:
        birth_day=datetime.datetime(year,month,day)
        current_user.profile.birth_day=birth_day
    current_user.save()
    current_user.profile.save()
    return HttpResponseRedirect(reverse('main:profile', ))
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('log_out',))
@login_required
def search_users(request):
    all_users=UserProfile.objects.all()                             
    searched_name=request.Post['searched_name']                         #The name that a user may search
    searched_first=searched_name.split()[0].lower()                     #We devided the name to first name and last name
    searched_last=searched_name.split()[1].lower()                      #We made all the names lowercase to make the search more accurate 
    most_relevant=[]                                                    #It's created to get all the most relevant searches
    for i in range(len(all_users)):
        if all_users[i].first_name.lower()==searched_first and all_users[i].last_name.lower()==searched_last:
            most_relevant.append[all_users[i]]
    return render(request, 'main/search.html',{'most_relevant':most_relevant})
@login_required
def send_post(request,topic_sub):
    user=request.user
    topic=Topic.objects.get(subject=topic_sub)
    content=request.POST['content']
    new_post=POST(author=user,content=content,topic=topic)
    new_post.save()
    return HttpResponseRedirect(reverse('main:topic', ),args=(topic_sub))
@login_required
def send_comment(request,post):
    content=request.POST['content']
    post=request.POST['post']
    user=request.user
    new_comment=Comment(autor=user,post=post,content=content)
    new_comment.save()
    return render(request, 'main_body/topic.html',{'user':current_user},)
def like_post(request,topic_sub):
    post_id=request.POST[post]
    post=Post.objects.get(pk=post_id)
    post.likes+=1
    return HttpResponseRedirect(reverse('main:topic' ,args=(topic_sub,)))


    
    
    
    
    
    
    
    
