from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home', views.home, name='home'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutUser, name='logout')
]
