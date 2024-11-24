from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse


def third_app_subdomain(request):
    return HttpResponse('third app view \n subdomain: "thirdapp" ')