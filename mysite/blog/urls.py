#django.conf.urls.defaults was deprecated
from django.conf.urls import *
from mysite.blog.views import archive
 

urlpatterns = patterns('',
    url(r'^$', archive),
)
