from django.db import models
from user.models import User
from django.forms import ModelForm

# Create your models here.

class Faq(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    id = models.ForeignKey()
    question = models.TextField(verbose_name="Soru")
    answer = models.TextField(verbose_name="Cevap", blank=True)
    status = models.CharField(choices=STATUS, verbose_name="Durum")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")

class Message(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
        ('New', 'Yeni'),
    )
    id = models.ForeignKey()
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='Yeni')
    email = User.email
    phone = models.CharField(max_length=15, verbose_name="Telefon Numarası")
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=300)
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")


class CommentForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'comment']