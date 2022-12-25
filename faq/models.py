from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Faq(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    question = models.CharField(max_length=50, blank=True)
    answer = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, verbose_name="Durum")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")

class Message(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
        ('New', 'Yeni'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='Yeni')
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=300)
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
