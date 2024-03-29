from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from core import utils

def request_to_response(request, template, context={}):
    # ensure we have the environment var set
    context.update(environment=utils.get_environment_data(request))
    context.update(environments=settings.ENVIRONMENTS)
    return render_to_response(
        template,
        context,
        context_instance=RequestContext(request)
    )