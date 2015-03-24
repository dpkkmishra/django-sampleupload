from django.conf.urls import patterns, url


urlpatterns = patterns(
    'demo.views',
    url(r'^$', 'home'),
    url(r'^create_post/$', 'create_post'),
    
)
