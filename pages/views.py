"""
Jordyn Kuhn
CIS 218 Web Application Programming
1-22-2023
"""

from django.views.generic import TemplateView

class homePageView(TemplateView):
    template_name = "home.html"

class projectPageView(TemplateView):
    template_name = "project.html"

class contactPageView(TemplateView):
    template_name = "contact.html"