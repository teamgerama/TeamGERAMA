from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('programme/<int:pk>/', views.programme_detail, name='programme_detail'),
]