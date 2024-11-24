from django.urls import path

from .views import third_app_subdomain

urlpatterns = [
    path('subdomain/', third_app_subdomain, name='third_app_subdomain')
]