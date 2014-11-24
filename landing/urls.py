from django.conf.urls import patterns, include, url
from landing.views import landing_render, send_order

urlpatterns = patterns('landing.views',
    url(r'^$', 'landing_render'),
    url(r'^send-order/$', 'send_order')
)