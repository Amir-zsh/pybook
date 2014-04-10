from django.contrib import admin
from accounts.models import UserProfile
from django.contrib.auth.models import User
# class UserAdmin(admin.ModelAdmin):
#     fields=['username','password','first_name','last_name','email']
admin.site.register(UserProfile)



