from django.db import models
from ..user.models import User
# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    id = models.ForeignKey("auth.user", on_delete=models.CASCADE, verbose_name="Kategori Id")
    parent_id = models.TextChoices('Kategori', 'Sağlık Teknoloji Eğitim')
    title = models.CharField(max_length=50, verbose_name="Kategori Başlığı")
    keywords = models.TextField(blank=True, verbose_name="Anahtar Kelimeler")
    description = models.TextField(blank=True, verbose_name="Kategori Tanımı")
    image = models.ImageField(blank=True, upload_to='images/',verbose_name="Kategori Resmi")
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")
    def __str__(self):
        return self.title

class Projeler(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    id = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Proje Id")
    title = models.CharField(max_length=50, verbose_name="Proje Başlığı")
    keywords = models.TextField(blank=True, verbose_name="Anahtar Kelimeler")
    description = models.TextField(blank=True, verbose_name="Proje Tanımı")
    image = models.ImageField(blank=True, verbose_name="Proje Fotoğrafı")
    category_id = Category.id
    detail = models.TextField(verbose_name="Proje Detayları")
    videolink = models.URLField(verbose_name="Video Linki")
    userid = User.id
    status = models.CharField(choices=STATUS, verbose_name="Durum")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")
    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    id = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yorum Id")
    comment = models.TextField(verbose_name="Yorum")
    rate = models.IntegerField(min=0, max=5, verbose_name="Puan")
    project_id = Projeler.id
    user_id = User.id
    ip = models.IPAddressField(verbose_name="IP Adresi")
    status = models.CharField(choices=STATUS, verbose_name="Durum")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")
    def __str__(self):
        return self.rate

class Image(models.Model):
    id = models.ForeignKey("auth.user", on_delete=models.CASCADE, verbose_name="Resim id")
    project_id = Projeler.id
    title = models.CharField(max_length=30, verbose_name="Resim Başlığı")
    image = models.ImageField(verbose_name="Resim")
    def __str__(self):
        return self.title
