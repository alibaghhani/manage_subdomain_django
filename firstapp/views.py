from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def default_subdomain_view(request):
    return HttpResponse("no subdomains \n default host www")