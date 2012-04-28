from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import OrderForm

#---------------------------------------------------------------------------
def order_list(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form.save()
    context = dict(
        form=form
    )
    return render_to_response(
        'order/index.html',
        context,
        context_instance=RequestContext(request)
    )
