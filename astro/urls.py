from django.conf.urls.defaults import *
from astro.views import get_astro

urlpatterns = patterns('',
   url(r'^get_astro/$', get_astro),
)

