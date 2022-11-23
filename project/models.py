from django.db import models
from ..user.models import User

# Create your models here.

class Projeler(models.Model):
    id = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Proje Id")
    title = models.CharField(max_length=50, verbose_name="Proje Başlığı")
    keywords = models.TextField(verbose_name="Anahtar Kelimeler")
    description = models.TextField(verbose_name="Proje Tanımı")
    image = models.ImageField(verbose_name="Proje Fotoğrafı")
    category_id = category.models.id
    detail = models.TextField(verbose_name="Proje Detayları")
    videolink = models.URLField(verbose_name="Video Linki")
    userid = User.id
    status = models.BooleanField(verbose_name="Durum")
    created_at = models.DateTimeField(auto_created=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Son Güncellenme Tarihi")
    def __str__(self):
        return self.title
