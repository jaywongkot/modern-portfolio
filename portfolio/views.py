from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio.html'
    # We changed a context variable from object_list to all_project_all
    context_object_name = 'all_project_list'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
