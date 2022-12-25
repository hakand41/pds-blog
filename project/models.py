from django.db import models
# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    parent_id = models.TextChoices('Kategori', 'Sağlık Teknoloji Eğitim')
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length=50)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Projeler(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(blank=True, max_length=50)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = models.TextField()
    videolink = models.CharField(max_length=50, blank=True)
    status = models.CharField(choices=STATUS, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    project = models.ForeignKey(Projeler, on_delete=models.CASCADE)
    comment = models.TextField()
    subject = models.CharField(max_length=50)
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=True)
    status = models.CharField(choices=STATUS, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")
    def __str__(self):
        return self.subject

class Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title
