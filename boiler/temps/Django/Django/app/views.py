from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def ping(request):
    return HttpResponse('OK', status=200)

def index(request):
    data='{"status":"success","data":[{"id":1,"employee_name":"Tiger Nixon","employee_salary":320800,"employee_age":61,"profile_image":""},{"id":2,"employee_name":"Garrett Winters","employee_salary":170750,"employee_age":63,"profile_image":""}],"message":"Successfully! All records has been fetched."}'
    return HttpResponse(data)