from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
