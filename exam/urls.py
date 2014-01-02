from django.conf.urls.defaults import *
from exam.views import get_types,get_qeustions

urlpatterns = patterns('',
   url(r'^types/$', get_types),
   url(r'^questions/$', get_qeustions),
)

