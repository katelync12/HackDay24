from django.contrib import admin
from django.urls import path
from babybytes import views

urlpatterns = [
    path("", views.home_view, name="index"),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
]
