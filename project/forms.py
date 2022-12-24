from django import forms
from project.models import Projeler

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projeler
        fields = ["title", "keywords", "description", "image", "detail", "videolink", "status"]
    
