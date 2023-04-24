from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile, UserInfo, Rating, Post
# Register your models here.


# Registered Users with Profile
admin.site.register(Profile)
admin.site.register(UserInfo)
admin.site.register(Post)
admin.site.register(Rating)
