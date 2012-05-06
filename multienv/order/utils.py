from django import http

from core import utils

from models import Order

#---------------------------------------------------------------------------
def order_or_404(func):
    """Check that order is exists, if not return 404"""
    def decorator(request, order_id, *args, **kwargs):
        try:
            order = Order.objects.using(utils.get_environment_db(request)).get(
                pk=order_id
            )
            return func(request, order, *args, **kwargs)
        except Order.DoesNotExist():
            return http.HttpResponseNotFound("Order Not Found")
    return decorator