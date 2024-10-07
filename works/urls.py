from django.urls import path
from . import views

urlpatterns = [
    path('authorization', views.authorization, name='authorization'),
    path('home_page', views.home_page, name='home-page'),
    path('add_service', views.add_service, name='add-service'),
    path('add_work', views.add_work, name='add-work'),
    path('delete_service/<str:pk>/', views.delete_service, name="delete-service"),
    path('update_service/<str:pk>/', views.update_service, name="update-service"),
    path('result', views.result, name="result"),
    path('reset', views.reset, name="reset"),
]
