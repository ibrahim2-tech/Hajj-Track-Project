# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), # Setting login as your home page
    path('register/', views.register_view, name='register'),
    path('campaigns/', views.services_list, name='services_list'),
    path('add/', views.add_service, name='add'),
    path('detail/<int:service_id>/', views.service_detail, name='detail'),
    path('update/<int:service_id>/', views.update_service, name='update'),
    path('delete/<int:service_id>/', views.delete_service, name='delete'),
    path('logout/', views.logout_view, name='logout'),
]