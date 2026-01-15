from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('create/', views.create_service, name='create_service'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('service/edit/<int:service_id>/', views.edit_service, name='edit_service'),
    
]