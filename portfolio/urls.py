from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='portfolio'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<category>/', views.project_category, name='project_category'),
]
