from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import News

def index(request):
    #return HttpResponse("Personalized university news and announcement delivery service")
    #template = loader.get_template('news/index.html')
    return render(request,'news/index.html')

def activity(request):
	activity_news = News.objects.all()
	#template = loader.get_template('news/activity.html')
	#context = RequestContext(request,{
	#	'activity_news': activity_news,
	#})
	#output = ', '.join([p.activity for p in activity_news])
	#return HttpResponse(template.render(context))
	return render(request,'news/activity.html',{'activity_news':activity_news})
