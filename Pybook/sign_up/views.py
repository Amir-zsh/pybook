from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
class Sign_up_view(generic.DetailView):
	model=User
	template_name='sign_up/sign_up.html'
def user_sign_up(request):
	username=request.POST['username']
	password=request.POST['password']
	email=request.POST['email']
	first_name=request.POST['first_name']
	last_name=request.POST['last_name']
	status=request.POST['satus']
	birth_day=request.POST['birth_day']
	user=User.objects.create_user(username, email, password)
	user_profile=UserProfile(user=user,birth_day=birth_day,status=status)
	return HttpResponseRedirect(reverse('main_site:profiles', args=(username,)))


	
	

# Create your views here.