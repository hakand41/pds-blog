from django.db import models

# Create your models here.

class User(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    id = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Proje Sahibi")
    name = models.CharField(max_length=20, verbose_name="İsim")
    surname = models.CharField(max_length=20, verbose_name="Soyisim")
    email = models.EmailField(verbose_name="E-Posta Adresi")
    password = models.CharField(max_length=32, verbose_name="Şifre")
    status = models.CharField(choices=STATUS, verbose_name="Durum")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")
    def __str__(self):
        return self.name

class Profile(models.Model):
    id = models.ForeignKey()
    user_id = User.id
    image = models.ImageField(verbose_name="Profil Resmi")
    address = models.TextField(verbose_name="Adres")
    phone = models.TextField(verbose_name="Telefon")
    profile_type = models.TextChoices('Type', 'User Faculty')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Güncellenme Tarihi")
    def __str__(self):
        return self.user_id
