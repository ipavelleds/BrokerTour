from django.conf.urls import patterns, include, url
from django.contrib import admin
import landing

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BrokerTour_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('landing.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

import settings
if settings.DEBUG:
    # set static handler
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)