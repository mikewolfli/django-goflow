from django.conf.urls import *

urlpatterns = patterns('',
    (r'^processimage/(?P<process_id>.*)/pos_activity/$', 'goflow.graphics2.views.pos_activity'),
)
