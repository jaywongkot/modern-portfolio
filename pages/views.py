from django.views.generic import TemplateView


class HomePageView(TemplateView):  # new
    template_name = 'home.html'


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'


class ContactPageView(TemplateView):  # new
    template_name = 'contact.html'
