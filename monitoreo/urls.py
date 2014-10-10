from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from os import path as os_path
from settings import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^monitoreo/', include('monitoreo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'monitoreo.encuestas.views.index'),
    url(r'^', include('monitoreo.encuestas.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^xls/$', 'monitoreo.utils.save_as_xls'),
    url(r'^', include('noticias.urls')),

)

handler404 = 'monitoreo.views.file_not_found_404'

handler500 = 'monitoreo.views.file_not_found_500'

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )