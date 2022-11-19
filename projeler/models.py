from django.db import models

# Create your models here.

class Projeler(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    proje = models.FileField()
    release_date = models.DateTimeField(auto_now_add=True)