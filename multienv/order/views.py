from core.shortcuts import request_to_response

from forms import OrderForm

#---------------------------------------------------------------------------
def order_list(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form.save(request=request)
    context = dict(
        form=form
    )
    return request_to_response(request, 'order/index.html', context)
