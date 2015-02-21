#django.conf.urls.defaults was deprecated
from django.conf.urls import *
from mysite.blog.views import archive, add_topic
 

urlpatterns = patterns('',
    url(r'^$', archive),
    url(r'^addpost$', add_topic),
)
