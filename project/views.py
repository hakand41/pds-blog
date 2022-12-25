from django.shortcuts import render, HttpResponse, redirect
from .forms import ProjectForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html") 

def about(request):
    return render(request, "about.html") 

def detailProject(request,id):
    return HttpResponse("Detail:" + str(id))

def project(request):
    return render(request, "projects.html")

def dashboard(request):
    return render(request, "dashboard.html")

def addProject(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.author = request.user
        project.save()
        messages.success(request, "Proje başarıyla eklendi")
        return redirect("index")
    return render(request, "addproject.html", {"form" : form})
