from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_lenghth=50)
    description = models.CharField(max_lenghth=500)
    company = models.CharField(max_lenghth=50)
    adress = models.CharField(max_lenghth=150, blank=True)
    fax = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=50)
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    aboutus = models.CharField(max_lenghth=50, blank=True)
    contact = models.CharField(max_lenghth=50, blank=True)
    references = models.CharField(max_lenghth=50, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title