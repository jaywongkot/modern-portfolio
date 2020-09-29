from django.views.generic import ListView
from .models import Project


class PortfolioPageView(ListView):
    model = Project
    template_name = 'portfolio.html'
