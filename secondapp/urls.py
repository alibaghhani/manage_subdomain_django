from django.urls import path

from .views import second_app_subdomain

urlpatterns = [
    path('subdomain/', second_app_subdomain, name='second_app_subdomain')
]