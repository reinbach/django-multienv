from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^order/', include('order.urls')),
    url(r'^profile/', include('profile.urls')),
    url(
        r'^environment/(?P<env>\w+)/$',
        'core.views.change_environment',
        name='change_environment'
    ),
    url(r'^$', 'core.views.home', name='home'),
)

urlpatterns += staticfiles_urlpatterns()