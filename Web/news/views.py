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
	fund_list = News.objects.all()
	return render(request,'news/fund.html',{'fund_news':fund_list})

def funds(request):
	fund_list = News.objects.all()
	return render(request,'news/fund.html',{'fund':fund})

def activity(request):
	activity_list = News2Sub.objects.filter(Sid_id=22)
	for i in activity_list:
		activity_news = News.objects.filter(Nid=i.Nid_id)
	return render(request,'news/activity.html',{'activity_news':activity_news})

def announce(request):
	announce_list = Subcate.objects.filter(Cid=3)
	return render(request,'news/announce.html',{'announce_news':announce_news})

def test(request):
	return render(request,'news/test.html')

def testresult(request):
	post = request.POST.copy()
	id = post['TextBoxSTD_IDNO']
	link = "http://158.108.214.245/WebForm_report_std_B3.aspx?stdid="+id+"&link=1"

	return render(request,'news/testresult.html',{'link':link})