from django.views.generic import ListView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio.html'
    context_object_name = 'all_project_list'
