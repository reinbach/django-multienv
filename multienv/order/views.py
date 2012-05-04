from django import http
from django.contrib import messages
from django.core.urlresolvers import reverse

from core.shortcuts import request_to_response
from core import utils

from forms import OrderForm

#---------------------------------------------------------------------------
def order_list(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, "Successfully added order to {env}".format(
                env=utils.get_environment_data(request).get('label')
            ))
            return http.HttpResponseRedirect(reverse('order_home'))
    context = dict(
        form=form
    )
    return request_to_response(request, 'order/index.html', context)
