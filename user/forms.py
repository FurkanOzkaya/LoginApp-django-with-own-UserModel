from django import forms
from django.core.validators import EmailValidator,MaxLengthValidator,MinLengthValidator
from Process.validations import *
from .DataAccess.UserDataAccess import get_user_replacate_by_email,get_user_replacate_by_phone_number

class RegisterForm(forms.Form):
    e_mail=forms.CharField(max_length=50,label="E-Mail")
    password=forms.CharField(max_length=75,label="Şifre",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=75,label="Şifre Tekrar",widget=forms.PasswordInput)
    first_name=forms.CharField(max_length=30,label="Ad")
    last_name=forms.CharField(max_length=30,label="Soyad",required=False)
    phone_number=forms.CharField(max_length=20,label="Telefon Numarası",required=False)
    #image=forms.ImageField(max_length=100,label="Profil Fotoğrafı",required=False)

    

    def clean(self):
        e_mail=self.cleaned_data.get("e_mail")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        last_name=self.cleaned_data.get("last_name")
        first_name=self.cleaned_data.get("first_name")
        phone_number=self.cleaned_data.get("phone_number")

        if  is_password_valid(password=password)==False:   
            raise forms.ValidationError("Şifre En az 5 En Çok 50 Karakter Olmalı")
        if password and confirm and password!=confirm:
            raise forms.ValidationError("Şifreler Eşleşmiyor")
        if  is_email_valid(e_mail=e_mail)==False:
            raise forms.ValidationError("E-Mail Adresi Geçersiz")
        if is_phone_number_valid(phone_number)==False:
            raise forms.ValidationError("Telefon Numarası Geçersiz")
        if get_user_replacate_by_email(e_mail):
            raise forms.ValidationError("E-mail Adresi Kullanılıyor")
        if phone_number!="":
            if  get_user_replacate_by_phone_number(phone_number):
                raise forms.ValidationError("Telefon Numarası Kullanılıyor")
        

        else:
            values={
            "e_mail":e_mail,
            "password":password,
            "first_name":first_name,
            "last_name":last_name,
            "phone_number":phone_number,
       }

            return values
        


class LoginForm(forms.Form):
    e_mail=forms.CharField(max_length=50,label="E-Mail")
    password=forms.CharField(max_length=75,label="Şifre",widget=forms.PasswordInput)