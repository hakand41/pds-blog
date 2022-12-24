from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html", {"number":7}) 

def about(request):
    return render(request, "about.html") 

def detailProject(request,id):
    return HttpResponse("Detail:" + str(id))
