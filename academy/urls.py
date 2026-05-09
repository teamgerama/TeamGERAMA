from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.school_list, name='resources'),
    path('school/<int:school_id>/', views.school_detail, name='school_detail'),
    path('department/<int:dept_id>/', views.dept_detail, name='dept_detail'),
    path('programme/<int:pk>/', views.programme_detail, name='programme_detail'),
    path('programme/<int:pk>/level/<str:level>/', views.level_detail, name='level_detail'),
    path('programme/<int:pk>/level/<str:level>/semester/<str:semester>/', views.semester_detail, name='semester_detail'),
]