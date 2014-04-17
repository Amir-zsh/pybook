from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.utils import timezone
import datetime
class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True, related_name='profile')
	first_name=models.CharField(blank=True,max_length=30)
	last_name=models.CharField(blank=True,max_length=30)
	birth_day= models.DateTimeField(blank=True,null=True)
	following=models.ManyToManyField(User,related_name='follower')
	photo=models.ImageField(blank=True,null=True,upload_to='photos')
	status=models.TextField(blank=True)
	def __unicode__(self):
		return self.user.username

