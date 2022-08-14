from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'acnt'

urlpatterns = [
    path('signup/', views.CustomSignup.as_view(), name='signup'),
    path('login/', views.CustomLogin.as_view(), name='login'),
    path('logout/', views.CustomLogout.as_view(), name='logout'),
    # path('account/<int:pk>/', views.MyAccountViews.as_view(), name='account'),
    path('account/<slug:slug>/', views.MyAccountViews.as_view(), name='account')
]