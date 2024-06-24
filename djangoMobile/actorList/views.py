from django.http import HttpResponse
from .models import Actor
from django.core import serializers


def index(request):
    return HttpResponse("API V.1")


def api(request):
    contents = Actor.objects.all()
    jsonData = serializers.serialize('json', contents)
    return HttpResponse(jsonData, 
                        content_type='application/json')
