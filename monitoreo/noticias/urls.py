from django.conf.urls.defaults import *
from django.conf import settings
from models import Noticia

urlpatterns = patterns('monitoreo.noticias.views',
    #(r'^rss/$', NoticiasFeed()),
    #(r'^noticias/binacional/feed/$', NoticiasBinacionalFeed()),
    (r'^noticias/$', 'noticia_lista'),
    (r'^noticias/(?P<slug>[-\w]+)/$', 'noticia_detalle'),
    (r'^noticias/categoria/(?P<cat_slug>[-\w]+)/$', 'noticia_lista_cat'),
    # (r'^noticias/tipo/(?P<tipo>[-\w]+)/$$', 'noticia_lista_tipo'),
    # (r'^noticias/comentarios/', include('django.contrib.comments.urls')),
)
