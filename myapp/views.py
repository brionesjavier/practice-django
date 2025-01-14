from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    title = "Bienvenido a mi pagina web"

    return render(request,'index.html',{'title': title})


def hello(request, username):
    #print(username)
    #return HttpResponse("<h2>hello %s</h2>" % username)
    return render(request,'hello.html',{'username':username})


def about(request):
    return HttpResponse("About")

def project(request):
    #projects = Project.objects.all()
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False);

def task(request,id):
    #task= Task.objects.get(id=id)

    task= get_object_or_404(Task,id=id)
    return HttpResponse("task: %s" % task.title);
