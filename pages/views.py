from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Home")

def projectPageView(request):
    return HttpResponse("Projects")

def contactPageView(request):
    return HttpResponse("Contact")