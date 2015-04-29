from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
#from django.views.generic.simple import redirect_to
from news import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^fund$', views.fund, name='fund'),
    url(r'^activity$', views.activity, name='activity'),
    url(r'^announce$', views.announce, name='announce'),
    url(r'^nisit$',views.nisit),
    url(r'^result$',views.result),
    #redirect any page don't have to index.html
    #url(r'^.*$', RedirectView.as_view(url='/news', permanent=False), name='index'), 
    #url(r'^.*$', redirect_to, {'url': 'http://www.google.com'}),

)
