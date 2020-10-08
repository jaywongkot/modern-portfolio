from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio.html'
    # We changed a context variable from object_list to all_projects_list
    context_object_name = 'all_projects_list'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
