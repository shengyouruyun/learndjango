from django.conf.urls import patterns, include, url

from django.contrib import admin

#from tweets import views
from tweets.views import Index, Profile, PostTweet, HashTagCloud, Search,\
 UserRedirect, MostFollowedUsers, TestEmail

from user_profile.views import Invite,InviteAccept

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytweets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^$', Index.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(\w+)/post/$', PostTweet.as_view()),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^hashTag/(\w+)/$', HashTagCloud.as_view()),
    url(r'^search/$', Search.as_view()),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^profile/$', UserRedirect.as_view()),
    url(r'^mostFollowers/$', MostFollowedUsers.as_view()),
    url(r'^email/$',TestEmail.as_view()),
    url(r'^invite/$', Invite.as_view()), 
    url(r'^invite/accept/(\w+)/$', InviteAccept.as_view()),    
)



