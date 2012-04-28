from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'profile.views.admin_list', name='profile_home'),
)