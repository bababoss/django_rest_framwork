from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Analysis
from snippets.serializers import SnippetSerializer
from django.template import loader
import simplejson
import datetime



#import forms
from .models import Analysis

from .forms import AnalysisForm

from django.conf import settings
from django.contrib.staticfiles import views

month1 = ['01','02','03']
year1 = ['2016','2017']


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    month1 = ['january','february','march','april','may','june','july','august','septmber','octomber','november','december']
    month = ['01','02','03']
    if request.method == 'GET':
        #snippets = Analysis.objects.filter(created__month=month[2],created__year=2016)
        snippets = Analysis.objects.filter(user_id__contains = 1023)
        #serializer = SnippetSerializer(snippets, many=True)
        serializer = SnippetSerializer(snippets, many=True)
        data1=serializer.data
        #snippets = Analysis.objects.filter(created__year__gte=2016)
        return JSONResponse(data1)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, month, year):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        #snippet = Analysis.objects.filter(created__month=month,created__year=year,created__day=4,created__hour__gte=9)
        snippet = Analysis.objects.filter(user_id__contains = 1030)
    except Analysis.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]
   
def index(request, month, year):

    query = Analysis.objects.filter(user_id__contains = 1030, created__month=month,created__year=year,created__day=5)
    j=1
    for i in query:
        if(j%2 != 0):
            print "odd===",j
            temp=i.created
            j+=1
        elif (j%2 == 0):
            print "even",j
            timediff = i.created - temp
            times=timediff.total_seconds()
            times+=times
            j+=1
            print "times is here ======",times/3600
        

    return render(request,'snippets/index.html', {})

def dashboard(request):
    
    if request.GET:
        data=request.GET
        print data['created']
#GET data from AnalysisForm
    
    form = AnalysisForm(request.GET)
    context = {
        'form': form,
        
    }


    
    return render(request, 'snippets/dashboard.html', context)
    
