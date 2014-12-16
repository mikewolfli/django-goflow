from django.conf.urls import *
from . import views

urlpatterns = patterns('',
    (r'^(?P<id>.*)/save/$', views.graph_save),
    (r'^(?P<id>.*)/$', views.graph, {'template':'goflow/graphics/graph.html'}),
)
