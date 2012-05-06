from django import http
from django.contrib import messages
from django.core.urlresolvers import reverse

from core.shortcuts import request_to_response
from core import utils

from forms import OrderForm
from models import Order
from utils import order_or_404

#---------------------------------------------------------------------------
def order_list(request):
    orders = Order.objects.using(utils.get_environment_db(request)).all()
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
        form=form,
        orders=orders
    )
    return request_to_response(request, 'order/index.html', context)

#---------------------------------------------------------------------------
@order_or_404
def order_edit(request, order):
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, "Successfully updated order in {env}".format(
                env=utils.get_environment_data(request).get('label')
            ))
            return http.HttpResponseRedirect(reverse('order_home'))
    context = dict(
        form=form,
    )
    return request_to_response(request, 'order/edit.html', context)

#---------------------------------------------------------------------------
@order_or_404
def order_delete(request, order):
    order.delete()
    messages.success(request, "Successfully deleted order in {env}".format(
        env=utils.get_environment_data(request).get('label')
    ))
    return http.HttpResponseRedirect(reverse('order_home'))
    
    