from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^fund$', views.fund, name='fund'),
    url(r'^activity$', views.activity, name='activity'),
    url(r'^announce$', views.announce, name='announce'),
    url(r'^test$',views.test),
    url(r'^testresult$',views.testresult),
)
