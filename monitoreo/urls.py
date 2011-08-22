from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from os import path as os_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^monitoreo/', include('monitoreo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^xls/$', 'monitoreo.utils.save_as_xls'),
    (r'^$', 'monitoreo.encuestas.views.index'),
    (r'^', include('monitoreo.encuestas.urls')),
)

handler404 = 'monitoreo.views.file_not_found_404'

handler500 = 'monitoreo.views.file_not_found_500'

urlpatterns += staticfiles_urlpatterns()
