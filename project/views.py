from django.shortcuts import render, HttpResponse, redirect
from .forms import ProjectForm
from django.contrib import messages
from .models import Projeler
# Create your views here.
def index(request):
    return render(request, "index.html") 

def about(request):
    return render(request, "about.html") 

def detailProject(request,id):
    projects = Projeler.objects.filter(id = id).first()
    return render(request, "detail.html", {"projects":projects})

def project(request):
    projects = Projeler.objects.filter()
    context = {
        "projects":projects
    }
    return render(request, "projects.html", context)

def dashboard(request):
    projects = Projeler.objects.filter(author = request.user)
    context = {
        "projects":projects
    }
    return render(request, "dashboard.html", context)

def addProject(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.author = request.user
        project.save()
        messages.success(request, "Proje başarıyla eklendi")
        return redirect("index")
    return render(request, "addproject.html", {"form" : form})
