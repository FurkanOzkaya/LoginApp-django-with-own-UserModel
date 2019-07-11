from django.shortcuts import render,HttpResponse,redirect
from django.contrib import sessions
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from .models import User
from .DataAccess.UserDataAccess import createUser
from django.contrib.auth import login as login_session
from django.contrib.auth import authenticate
from django.core.validators import EmailValidator,MaxLengthValidator,MinLengthValidator
import hashlib
from Process.encrypt import *
from .DataAccess.Login_Logout_Backend import login_process,login_requried



def index(request):
    id=request.session.get("id",0)
    if id != 0:
        e_mail=request.session.__getitem__("e_mail")
        password=request.session.__getitem__("password")
        login_process(request,e_mail=e_mail,password=password)
    return  render(request,"index.html")


def register(request):
    form=RegisterForm(request.POST or None)

    if form.is_valid():
        e_mail = form.cleaned_data.get("e_mail")
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        phone_number = form.cleaned_data.get("phone_number")
        password=encrypt(value=password)
        # newUser=User(e_mail=e_mail,password=password,first_name=first_name,last_name=last_name,phone_number=phone_number)
        newUser=createUser(e_mail=e_mail,password=password,first_name=first_name,last_name=last_name,phone_number=phone_number)
        
        if newUser:
            login_session(request,newUser)
            messages.success(request,"Başarı İle Kayıt Oldunuz.")
            return redirect("index")
        else:
            messages.warning(request,"Kayıt Olma Başarısız Tekrar Deneyiniz")
            return redirect("user:register")
    context={
        "form":form
    }
    return render(request,"register.html",context)
def login(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        e_mail=form.cleaned_data.get("e_mail")
        password=form.cleaned_data.get("password")

        password=encrypt(value=password)
        user= login_process(request,e_mail=e_mail,password=password)

        if user is None:
            messages.warning(request,"Kullanıcı Adı veya Şifre Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarı İle Giriş Yaptınız..")
       # login_session(request,user)
        
        return redirect("index")

    return render(request,"login.html",context)


def logout(request):
    request.session.flush()

    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect("index")


def service(request):
    logged_in=login_requried(request)
    if logged_in==True:
        return render(request,"service.html")
    messages.warning(request,"Oturum Açmalısınız")
    return redirect("user:login")
