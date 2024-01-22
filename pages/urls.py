from django.urls import path
from .views import homePageView, projectPageView, contactPageView

urlpatterns=[
    path("", homePageView, name="home"),
    path("project/", projectPageView, name="project"),
    path("contact/", contactPageView, name="contact"),
]