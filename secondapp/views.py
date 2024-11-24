# Create your views here.
from django.http import HttpResponse


def second_app_subdomain(request):
    return HttpResponse('second app view \n subdomain: "secondapp" ')