from django import http
from django.conf import settings
from django.core.urlresolvers import reverse

from core.shortcuts import request_to_response
from core import utils

#---------------------------------------------------------------------------
def home(request):
    context = dict(
        environments=settings.ENVIRONMENTS,
    )
    return request_to_response(request, 'index.html', context)

#---------------------------------------------------------------------------
def change_environment(request, env):
    utils.set_environment(request, env)
    if next in request.GET:
        return http.HttpResponseRedirect(request.GET.get('next'))
    return http.HttpResponseRedirect(reverse('home'))