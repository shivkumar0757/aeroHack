from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import json
# Create your views here.


def ping(request):
    return HttpResponse("OK", status=200)

def index(request):
    print('index called')
    return render(request,'boiler/home.html')

def boiler_gen(request):
    print(request.POST)
    return HttpResponse(json.dumps(request.POST))