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
    myJson=json.loads(json.dumps(request.POST))
    print(type(myJson))
    print(myJson['frontend_opt'])
    if myJson['frontend_opt'] == 'React' and myJson['backend_opt'] == 'Flask':
        path_to_zip=get_file(request)
        file_name='FlaskReactTemp'
        response = HttpResponse(FileWrapper(open(path_to_zip,'rb')), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
            filename = file_name.replace(" ", "_")
        )
        return response
        
    del  myJson['csrfmiddlewaretoken']
    myJson['msg']= "Pair not supported"
    return HttpResponse('<h2>Pair Not supported yet</h2>'+str(myJson))



from shutil import make_archive
from wsgiref.util import FileWrapper
import os

def get_file(request):
    cwd=os.getcwd()
    files_path = cwd+"./boiler/temps/flask-react-boilerplate-master"
    print('----------------')
    print(os.getcwd())
    print(os.listdir('./boiler/temps') )
    path_to_zip = make_archive(files_path, "zip", files_path)
    return path_to_zip 