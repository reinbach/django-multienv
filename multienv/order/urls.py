from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'order.views.order_list', name='order_home'),
)