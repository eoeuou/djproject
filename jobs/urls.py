from django.conf.urls.defaults import *
from jobs.views import current_datetime,hours_ahead,hours_offset
from jobs.views import astro,astro_id

urlpatterns = patterns('',
   #url(r'^$', 'index'),
   #url(r'^(?P<job_id>\d+)/$', 'detail'),
    url(r'^index/','jobs.views.index'),
    url(r'^astro/$', astro),
    url(r'^astro/plus/(\d{1,2})/$', astro_id),
    url(r'^get_host_json/$', 'jobs.views.get_host_json'),
    url(r'^some_view/$', 'jobs.views.some_view'),
    url(r'^jobs_list/$', 'jobs.views.jobs_list'),
    url('^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^time/(plus|minus)(\d{1,2})hours/$',hours_offset),  
    url(r'^getCpp/$','jobs.views.getCpp')
)
