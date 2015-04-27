from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection
from news.models import News, Subcate,News2Sub
from itertools import chain

def index(request):
    #return HttpResponse("Personalized university news and announcement delivery service")
    #template = loader.get_template('news/index.html')
    return render(request,'news/index.html')

#def fund(request):
#	fund_list = News.objects.all()
#	return render(request,'news/fund.html',{'fund_news':fund_list})

def fund(request):
	#cursor = connection.cursor()
	#sql = "SELECT * FROM news_news INNER JOIN news_news2sub ON news_news.Nid = news_news2sub.Nid_id"
	#cursor.execute(sql)
	#row = cursor.fetchone()
	fund_all = News.objects.filter(Cid_id=1).order_by('-DatePublish')
	fund_110 = News2Sub.objects.filter(Sid_id=110)
	fund_120 = News2Sub.objects.filter(Sid_id=120)
	fund_130 = News2Sub.objects.all()
	fund_140 = News2Sub.objects.filter(Sid_id=140)
	fund_types = Subcate.objects.filter(Cid_id=1)
	return render(request,'news/fund.html',{'fund_110':fund_110,'fund_120':fund_120,'fund_130':fund_130, 'fund_140':fund_140,'fund_all':fund_all,'fund_types':fund_types})

def activity(request):
	activity_all = News.objects.filter(Cid_id=2).order_by('-DatePublish')
	activity_220 = News2Sub.objects.filter(Sid_id=220)
	activity_210 = News2Sub.objects.filter(Sid_id=210)
	activity_211 = News2Sub.objects.filter(Sid_id=211)
	activity_216 = News2Sub.objects.filter(Sid_id=216)
	activity_217 = News2Sub.objects.filter(Sid_id=217)
	return render(request,'news/activity.html',{'activity_all':activity_all,'activity_210':activity_210,'activity_216':activity_216,'activity_217':activity_217,'activity_220':activity_220})

def announce(request):
	announce_all = News.objects.filter(Cid_id=3)
	return render(request,'news/announce.html',{'announce_all':announce_all})

def test(request):
	return render(request,'news/test.html')

def testresult(request):
	post = request.POST.copy()
	id = post['TextBoxSTD_IDNO']
	link = "http://158.108.214.245/WebForm_report_std_B3.aspx?stdid="+id+"&link=1"

	return render(request,'news/testresult.html',{'link':link})