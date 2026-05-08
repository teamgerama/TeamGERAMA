from django.urls import path
from . import views

urlpatterns = [
    # The Landing Page (The green one we just built)
    path('', views.home, name='home'),

    # The Resources Entry Point (Should point to your school list view)
    # Replace 'views.school_list' if your function is named differently (e.g. views.index)
    path('resources/', views.school_list, name='resources'),

    # The Detail Page
    path('programme/<int:pk>/', views.programme_detail, name='programme_detail'),
]
