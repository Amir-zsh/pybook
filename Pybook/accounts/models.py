from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.utils import timezone
import datetime
class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True, related_name='profile')
	first_name=models.CharField(blank=True,max_length=30)
	last_name=models.CharField(blank=True,max_length=30)
	birth_day= models.DateTimeField(blank=True)
	photo=models.ImageField(upload_to='photos',blank=True)
	status=models.TextField(blank=True)
	def __unicode__(self):
		return self.user.username

