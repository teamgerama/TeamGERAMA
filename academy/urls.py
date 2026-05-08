from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # This path must exist for the 'Explore Resources' button to work
    path('resources/', views.home, name='resources'),
    path('programme/<int:pk>/', views.programme_detail, name='programme_detail'),
]