"""
URL configuration for multiuser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views
app_name="app1"
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name="home"),
    path('adminsignup',views.adminsignup,name="adminsignup"),
    path('studentsignup',views.adminsignup,name="studentsignup"),
    path('teachersignup',views.adminsignup,name="teachersignup"),
    path('adminhome', views.adminhome, name="adminhome"),
    path('studenthome', views.adminhome, name="studenthome"),
    path('teacherhome', views.adminhome, name="teacherhome"),
    path('login', views.user_login, name="login"),

 ]
