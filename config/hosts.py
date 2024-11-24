from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns(
    '',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'secondapp', 'secondapp.urls', name='secondapp_subdomain'),
    host(r'thirdapp', 'thirdapp.urls', name='thirdapp_subdomain')
)