from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'order.views.order_list', name='order_home'),
    url(r'^edit/(?P<order_id>\d+)/$', 'order.views.order_edit', name='order_edit'),
    url(r'^delete/(?P<order_id>\d+)/$', 'order.views.order_delete', name='order_delete'),
)