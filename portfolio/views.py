from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    # We changed a context variable from object_list to project_list
    context_object_name = 'project_list'
    template_name = 'portfolio.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
