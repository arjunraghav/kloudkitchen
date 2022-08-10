from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('quickmenu/', views.QuickMenuView.as_view(), name='quick_menu')
]