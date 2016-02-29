from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Analysis
from snippets.serializers import SnippetSerializer
import simplejson
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
    if request.method == 'GET':
        snippets = Analysis.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Analysis.objects.get(pk=pk)
    except Analysis.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
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
   
def index(request):
    snippets = Analysis.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    user_id=Analysis.objects.values('user_id')   #query for user id
    days=Analysis.objects.values('days')  #query for days

    user_id_dict = ValuesQuerySetToDict(user_id) #user_id serilization
    days_dict = ValuesQuerySetToDict(days)  # days_serilization
    
    user_id_json = simplejson.dumps(user_id_dict) # json encodind
    days_json = simplejson.dumps(list(days_dict)) #json encoding
    context = {
        'user_id': user_id_json,
        'days': days_json
        
    }
   
    return render(request,'snippets/index.html', {'data': serializer.data})