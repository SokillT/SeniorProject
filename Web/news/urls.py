from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
    url(u'^$',views.index,name='index'),
)
