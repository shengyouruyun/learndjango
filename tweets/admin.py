from django.contrib import admin

# Register your models here.

from models import Tweet, HashTag
from user_profile.models import User, UserFollowers

class TweetAdmin(admin.ModelAdmin):
	list_dispaly = ('user', 'text')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(HashTag)

admin.site.register(User)
admin.site.register(UserFollowers)


