from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)

def project_category(request, category):
    projects = Project.objects.filter(categories__name__contains=category)
    context = {
        'category': category,
        'projects': projects,
    }
    return render(request, 'project_category.html', context)
