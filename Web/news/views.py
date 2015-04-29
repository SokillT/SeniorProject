from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.db import connection
from news.models import News, Subcate,News2Sub
from itertools import chain

def index(request):
    fund_all = News.objects.order_by('-DatePublish')[0:10]
    #activity_all = News.objects.filter(Cid_id=2)[:5].order_by('-DatePublish')
    #announce_all = News.objects.filter(Cid_id=3)[:5].order_by('-DatePublish')
    return render(request,'news/index.html',{'fund_all':fund_all})#'activity_all':activity_all,'announce_all':announce_all})

def fund(request):
	f110 = []
	f120 = []
	f130 = []
	f140 = []
	fund_all = News.objects.filter(Cid_id=1).order_by('-DatePublish')
	fund_110 = News2Sub.objects.filter(Sid_id=110)
	fund_120 = News2Sub.objects.filter(Sid_id=120)
	fund_130 = News2Sub.objects.filter(Sid_id=130)
	fund_140 = News2Sub.objects.filter(Sid_id=140)
	for i in fund_110:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			f110.append(j.Nid)
	for i in fund_120:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			f120.append(j.Nid)
	for i in fund_130:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			f130.append(j.Nid)
	for i in fund_140:
		row= News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			f140.append(j.Nid)
	return render(request,'news/fund.html',{'f110':f110,'f120':f120,'f130':f130,'f140':f140,'fund_all':fund_all})

def activity(request):
	a220 = []
	a211 = []
	a216 = []
	a217 = []
	activity_all = News.objects.filter(Cid_id=2).order_by('-DatePublish')
	activity_220 = News2Sub.objects.filter(Sid_id=220)
	activity_211 = News2Sub.objects.filter(Sid_id=211)
	activity_216 = News2Sub.objects.filter(Sid_id=216)
	activity_217 = News2Sub.objects.filter(Sid_id=217)
	for i in activity_220:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			a220.append(j.Nid)
	for i in activity_211:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			a211.append(j.Nid)
	for i in activity_216:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			a216.append(j.Nid)
	for i in activity_217:
		row= News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			a217.append(j.Nid)
	return render(request,'news/activity.html',{'activity_all':activity_all,'a220':a220,'a211':a211,'a216':a216,'a217':a217})

def announce(request):
	an310 = []
	an320 = []
	an330 = []
	announce_all = News.objects.filter(Cid_id=3).order_by('-DatePublish')
	announce_310 = News2Sub.objects.filter(Sid_id=310)
	announce_320 = News2Sub.objects.filter(Sid_id=320)
	announce_330 = News2Sub.objects.filter(Sid_id=330)
	for i in announce_310:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			an310.append(j.Nid)
	for i in announce_320:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			an320.append(j.Nid)
	for i in announce_330:
		row = News.objects.filter(Nid=i.Nid_id)	
		for j in row:
			an330.append(j.Nid)
	return render(request,'news/announce.html',{'announce_all':announce_all,'an310':an310,'an320':an320,'an330':an330})

def nisit(request):
	return render(request,'news/nisit.html')

def result(request):
	post = request.POST.copy()
	id = post['TextBoxSTD_IDNO']
	link = "http://158.108.214.245/WebForm_report_std_B3.aspx?stdid="+id+"&link=1"
	#return render(request,'news/test.html')
	return HttpResponseRedirect(link)