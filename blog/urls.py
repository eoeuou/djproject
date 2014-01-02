from django.conf.urls.defaults import *
from blog.views import archive,get_now,get_books

urlpatterns = patterns('',
   url(r'^archive/$',archive),
   url(r'^books/$', get_books),
)

