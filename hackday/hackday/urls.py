from django.contrib import admin
from django.urls import path
from babybytes import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('questions/', views.question_view, name='questions'),
    path('about/', views.about_view, name='about'),
    path('account/', views.account_view, name='account'),
    path('message/', views.message_view, name='message'),
]
