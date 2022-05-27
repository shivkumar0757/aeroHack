from itertools import combinations
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

    combinations={'React':["Flask","SpringBoot","Node","Django"],    "Vue":["Flask","SpringBoot","Node","Django"],    "Angular":["Flask","SpringBoot","Node","Django"]}

    if myJson['frontend_opt'] in combinations and myJson['backend_opt'] in combinations[myJson['frontend_opt']]:
        path_to_zip=get_file(request,myJson['frontend_opt'],myJson['backend_opt'])
        file_name=myJson['backend_opt']+myJson['frontend_opt']+"Temp"
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
import zipfile

def get_file(request,front_end,back_end):
    cwd=os.getcwd()
    new_path=cwd+"./boiler/temps/"+front_end+"_"+back_end+".zip"
    print(new_path)
    print("hahahahahah")
    cwd+="./boiler/temps/"
    listfiles=[cwd+ front_end+".txt",cwd+back_end+".txt"]
    with zipfile.ZipFile(front_end+"_"+back_end+".zip",'w') as zip:
        for file in listfiles:
            zip.write(file,compress_type=zipfile.ZIP_DEFLATED)
    
    # return os.getcwd()+"./"+front_end+"_"+back_end+".zip"

    cwd=os.getcwd()
    files_path = cwd+"./boiler/temps/flask-react-boilerplate-master"
    print('----------------')
    print(os.getcwd())
    print(os.listdir('./boiler/temps') )
    path_to_zip = make_archive(files_path, "zip", files_path)
    print(path_to_zip)
    print("hahahaha")
    return path_to_zip 