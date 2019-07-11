from django.db import models
from django.utils.timezone import now as timezone

# Create your models here.

class User(models.Model):
    e_mail=models.CharField(max_length=50,verbose_name="E-Mail")
    password=models.CharField(max_length=50,verbose_name="Şifre")
    first_name=models.CharField(max_length=30,verbose_name="Ad",null=True,blank=True)
    last_name=models.CharField(max_length=30,verbose_name="Soyad",null=True,blank=True)
    is_active=models.BooleanField(default=True,verbose_name="Hesap Aktif")
    last_login=models.DateField(auto_now=True,verbose_name="Son Giriş Tarihi")
    phone_number=models.CharField(max_length=20,verbose_name="Telefon Numarası",null=True,blank=True)
    verification_code=models.IntegerField(verbose_name="Doğrulama Kodu",unique_for_year=True,null=True,blank=True)
    image=models.CharField(max_length=100,verbose_name="Profil Fotoğrafı",null=True,blank=True)

    
 



