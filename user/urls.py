from django.contrib import admin
from django.urls import path
from user import views
app_name="user"

urlpatterns = [
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('register/', views.register,name="register"),
    path('service/', views.service,name="service"),
]