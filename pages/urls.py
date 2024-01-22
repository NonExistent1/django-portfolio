"""
Jordyn Kuhn
CIS 218 Web Application Programming
1-22-2023
"""

from django.urls import path
from .views import contactPageView, homePageView, projectPageView

urlpatterns=[
    path("contact/", contactPageView.as_view(), name="contact"),
    path("", homePageView.as_view(), name="home"),
    path("project/", projectPageView.as_view(), name="project"),
]
    