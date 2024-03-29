from django.contrib import admin
from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path('', views.project, name = "project"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addproject/', views.addProject, name = "addproject"),
    path('project/<int:id>', views.detailProject, name="detail"),
    path('update/<int:id>', views.updateProject, name="update"),
    path('delete/<int:id>', views.deleteProject, name="delete"),
    path('comment/<int:id>', views.addComment, name="comment")
]