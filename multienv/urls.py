from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^order/', include('order.urls')),
    url(r'^profile/', include('profile.urls')),
)
