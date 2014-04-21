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
from django import forms
from django.db.models import Q


class ImageUploadForm(forms.Form):
    image = forms.ImageField()



def wall_view(request,user_name):
    user=User.objects.get(username=user_name)
    posts=Post.objects.filter(author=user).order_by('-pub_date')
    return render(request, 'main_body/Wall.html',{'current_user':request.user,'user':user,'posts':posts})
@login_required
def topic_view(request,topic_sub):
    topic=Topic.objects.get(subject=topic_sub)
    posts=Post.objects.filter(topic=topic).order_by('-pub_date')
    current_user=request.user
    if current_user.is_authenticated():
        return render(request, 'main_body/Topic.html',{'user':current_user,'topic':topic,'posts':posts},)
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
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    month=int(request.POST['Month'])
    year=int(request.POST['Year'])
    day=int(request.POST['Day'])
    country=request.POST['Country']
    bio=request.POST['bio']
    current_user=request.user
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            current_user.profile.photo= form.cleaned_data['image']
            current_user.profile.save()
            current_user.save()
            
        
    if password:
        current_user.set_password(password)
    if email:
        current_user.email=email
    if first_name:
        current_user.profile.first_name=first_name
    if last_name:
        current_user.profile.last_name=last_name
    if country:
        current_user.profile.country=country
    if bio:
        current_user.profile.status=bio
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
    searched_name=request.POST['searched_name']                         #The name that a user may search                   #We devided the name to first name and last name
    splited_list=searched_name.split()                    #We made all the names lowercase to make the search more accurate 
    searched_first=splited_list[0].lower()  
    most_relevant=[] 
    if len(splited_list)>1:
        searched_last=splited_list[1].lower() 
        for profile in all_users:
            if profile.first_name.lower()==searched_first and profile.last_name.lower()==searched_last:
                most_relevant.append(profile.user)
    else:
        for profile in all_users:
            if profile.first_name.lower()==searched_first:
                most_relevant.append(profile.user)
    return render(request, 'main_body/SearchResult.html',{'current_user':request.user,'most_relevant':most_relevant})

@login_required
def send_post(request,topic_id):
    user=request.user
    topic=Topic.objects.get(pk=topic_id)
    content=request.POST['content']
    new_post=Post(author=user,content=content,topic=topic)
    new_post.save()
    return HttpResponseRedirect(reverse('main:topic',args=(topic.subject,)))
    
@login_required
def send_comment(request,post_id):
    post=Post.objects.get(pk=post_id)
    content=request.POST['comment']
    user=request.user
    new_comment=Comment(author=user,post=post,content=content)
    new_comment.save()
    return HttpResponseRedirect(reverse('main:topic',args=(post.topic.subject,)))
def like_post(request,post_id):
    user=request.user
    post=Post.objects.get(pk=post_id)
    post.likes+=1
    post.save()
    return HttpResponseRedirect(reverse('main:topic',args=(post.topic.subject,)))
def unlike_post(request,post_id):
    user=request.user
    post=Post.objects.get(pk=post_id)
    post.liker.remove(user)
    post.likes-=1
    post.save()
    return HttpResponseRedirect(reverse('main:topic',args=(post.topic.subject,)))

def follow_user(request,user_name):
    current_user=request.user
    following_user=User.objects.get(username=user_name)
    current_user.profile.following.add(following_user)
    following_user.save()
    current_user.save()
    return HttpResponseRedirect(reverse('main:Your_Wall',args=(user_name,)))
@login_required    
def news_view(request):
    current_user=request.user
    followings=list(current_user.profile.following.all())
    raw_news=Post.objects.filter(Q(author=current_user) | Q(author__in=followings ))
    news=raw_news.order_by('-pub_date')
    return render(request, 'main_body/NEWS.html',{'user':current_user,'news':news,})
def topics_list_view(request):
    return render(request, 'main_body/TopicsMenu.html',{'user':request.user},)


        
    
    
    
    
    


    
    
    
    
    
    
    
    
