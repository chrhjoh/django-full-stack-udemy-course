from django.urls import path
from AppTwo import views

urlpatterns = [path('', views.index, name='index'),
               path('help/', views.help, name='help'),
               path('users/', views.users, name='help')]