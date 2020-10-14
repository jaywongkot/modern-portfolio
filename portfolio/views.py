from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Project

def project_list(request):
    projects = Project.objects.all().order_by('-pk')

    paginator = Paginator(projects, 4) # 4 project in each page
    page =request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)

    context = {
        'projects': projects,
        'page': page,
    }
    return render(request, 'portfolio.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)

def project_category(request, category):
    projects = Project.objects.filter(categories__name__contains=category).order_by('-pk')
    
    paginator = Paginator(projects, 4) # 4 project in each page
    page =request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)

    context = {
        'projects': projects,
        'category': category,
        'page': page,
    }
    return render(request, 'project_category.html', context)
