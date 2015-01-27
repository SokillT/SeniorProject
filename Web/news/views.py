from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    #return HttpResponse("Personalized university news and announcement delivery service")
    #template = loader.get_template('news/index.html')
    return render(request,'news/index.html')
