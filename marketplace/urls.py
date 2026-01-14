from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('create/', views.create_service, name='create_service'),
]