from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wash/', views.wash, name='wash'),
    path('tire-service/', views.tire_service, name='tire-service'),
    path('tire-service/', views.tire_service, name='tire-service'),
    path('service/', views.service, name='service'),
]
