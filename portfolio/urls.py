from django.urls import path
from .views import PortfolioPageView

urlpatterns = [
    path('', PortfolioPageView.as_view(), name='portfolio'),
]
