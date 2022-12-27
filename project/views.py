from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Projeler, Comment
# Create your views here.
def index(request):
    projects = Projeler.objects.all()
    context = {
        "projects":projects
    }
    return render(request, "index.html", context) 

def about(request):
    return render(request, "about.html") 

def detailProject(request,id):
    projects = Projeler.objects.filter(id = id).first()
    #projects = get_object_or_404(Projeler, id = id)
    comments = projects.comments.all()
    return render(request, "detail.html", {"projects":projects, "comments":comments})

def project(request):
    keyword = request.GET.get("keyword")
    if keyword:
        projects = Projeler.objects.filter(title__contains = keyword)
        return render(request, "projects.html", {"projects":projects})
    projects = Projeler.objects.all()
    context = {
        "projects":projects
    }
    return render(request, "projects.html", context)

@login_required(login_url="user:login")
def dashboard(request):
    projects = Projeler.objects.filter(author = request.user)
    context = {
        "projects":projects
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addProject(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.author = request.user
        project.save()
        messages.success(request, "Proje başarıyla eklendi")
        return redirect("index")
    return render(request, "addproject.html", {"form" : form})

@login_required(login_url="user:login")
def updateProject(request, id):
    project = get_object_or_404(Projeler, id = id)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if form.is_valid():
        project = form.save(commit=False)
        project.author = request.user
        project.save()
        messages.success(request, "Proje başarıyla güncellendi")
        return redirect("index")
    return render(request, "update.html", {"form":form})

@login_required(login_url="user:login")
def deleteProject(request, id):
    project = get_object_or_404(Projeler, id = id)
    project.delete()
    messages.success(request, "Proje başarıyla silindi")
    return redirect("index")

@login_required(login_url="user:login")
def addComment(request, id):
    project = get_object_or_404(Projeler, id = id)
    if request.method == "POST":
        subject = request.POST.get("subject")
        comment = request.POST.get("comment")
        newComment = Comment(subject = subject, comment = comment, user_id = request.user)
        newComment.project = project
        newComment.save()
    return redirect("/projects/project/" + str(id))
