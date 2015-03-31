from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import News, Subcate

def index(request):
    #return HttpResponse("Personalized university news and announcement delivery service")
    #template = loader.get_template('news/index.html')
    return render(request,'news/index.html')

def fund(request):
	fund_list = Subcate.objects.filter(Cid=1)
	return render(request,'news/fund.html',{'fund_news':fund_news})

def activity(request):
	activity_list = Subcate.objects.filter(Cid=2).order_by('-Nid')
	return render(request,'news/activity.html',{'activity_news':activity_news})

def announce(request):
	announce_list = Subcate.objects.filter(Cid=3)
	return render(request,'news/announce.html',{'announce_news':announce_news})

