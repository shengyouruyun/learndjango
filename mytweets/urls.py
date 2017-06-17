from django.conf.urls import patterns, include, url

from django.contrib import admin

#from tweets import views
from tweets import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytweets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.Index.as_view()),
    url(r'^admin/', include(admin.site.urls)),)
