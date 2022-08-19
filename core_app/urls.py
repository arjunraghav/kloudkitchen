from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('quickmenu/', views.QuickMenuView.as_view(), name='quick_menu'),

    path('managemenu/add/', views.ManageMyMenuVendorCuisineCreateView.as_view(), name='manage_menu_add'),
    path('managemenu/list/', views.ManageMyMenuVendorCuisineListView.as_view(), name='manage_menu_list'),

    path('managemenu/add/dish_cat/', views.ManageMyMenuVendorDishCatCreateView.as_view(), name='manage_menu_add_dish_cat'),
    path('managemenu/list/dish_cat/', views.ManageMyMenuVendorDishCatListView.as_view(), name='manage_menu_list_dish_cat'),

    path('managemenu/add/dish/', views.ManageMyMenuVendorDishCreateView.as_view(), name='manage_menu_add_dish'),
    path('managemenu/list/dish/', views.ManageMyMenuVendorDishListView.as_view(), name='manage_menu_list_dish'),

    path('managemenu/create_menu_id', views.VendorMenuIdCreateView.as_view(), name='manage_menu_create_menu_id'),
    path('managemenu/create_menu', views.VendorMenuCreateView.as_view(), name='manage_menu_create_menu'),

    # path('managemenu/new/', views.NewManageMyMenuTemplateView.as_view(), name='new_manage_menu_template'),
    # path('managemenu/new/add/', views.NewManageMyMenyCreateView.as_view(), name='new_manage_menu_create'),
]