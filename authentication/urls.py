from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user_login ,name="login"),
    path('user_login/',views.user_login,name="user_login"),
    path('base_file/',views.base_file,name="base_file"),
    path('user_logout',views.user_logout,name="user_logout")
    
    
 ]
