from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('', ProjectListView.as_view(), name='portfolio'),
]
