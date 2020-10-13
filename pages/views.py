from django.shortcuts import render

def index(request):
    """The home page for modern portfolio"""
    return render(request, 'home.html')

def about(request):
    """The about page for modern portfolio"""
    return render(request, 'about.html')

def contact(request):
    """The contact page for modern portfolio"""
    return render(request, 'contact.html')