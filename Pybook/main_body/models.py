from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Topic(models.Model):
    creator=models.ForeignKey(User,related_name='topic')
    subject=models.CharField(max_length=100)
    pub_date=models.DateTimeField(default=timezone.now())


class Post(models.Model):
    author=models.ForeignKey(User,related_name='post')
    pub_date=models.DateTimeField(default=timezone.now())
    topic=models.ForeignKey(Topic,related_name='post')
    content=models.TextField()
    likes=models.IntegerField(default=0)
    def __unicode__(self):
        return pub_date
    
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment')
    author=models.ForeignKey(User,related_name='comment')
    pub_date=models.DateTimeField(default=timezone.now())
    content=models.TextField()
    likes=models.IntegerField(default=0)
    def __unicode__(self):
        return pub_date
    
class Private_message(models.Model):
    author=models.ForeignKey(User,related_name='sent_pm')
    pub_date=models.DateTimeField(default=timezone.now())
    content=models.TextField()
    receiver=models.ForeignKey(User,related_name='recivied_pm')
    def __unicode__(self):
        return pud_date
    

    
    
    
    
    



