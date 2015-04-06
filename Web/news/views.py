from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import News, Subcate, News2Sub

def index(request):
    #return HttpResponse("Personalized university news and announcement delivery service")
    #template = loader.get_template('news/index.html')
    return render(request,'news/index.html')

def fund(request):
	fund_list = Subcate.objects.filter(Cid=1)
	return render(request,'news/fund.html',{'fund_news':fund_list})

def activity(request):
	activity_list = News2Sub.objects.filter(Sid_id=22)
	for i in activity_list:
		activity_news = News.objects.filter(Nid=i.Nid_id)
	return render(request,'news/activity.html',{'activity_news':activity_news})

def announce(request):
	announce_list = Subcate.objects.filter(Cid=3)
	return render(request,'news/announce.html',{'announce_news':announce_news})

