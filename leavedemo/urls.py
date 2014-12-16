from django.conf.urls import patterns,url,include
from django.conf import settings
from django.views.generic.base import  RedirectView,TemplateView

from .leave.forms import StartRequestForm, RequesterForm, CheckRequestForm

from os.path import join, dirname
_dir = join(dirname(__file__))

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # FOR DEBUG AND TEST ONLY
    url(r'^.*/accounts/login.*switch/(?P<username>.*)/(?P<password>.*)/$', 'goflow.workflow.views.debug_switch_user', {'redirect':'/leave/'}),
    url(r'^.*/switch/(?P<username>.*)/(?P<password>.*)/$', 'goflow.workflow.views.debug_switch_user'),
    # user connection
    url(r'^.*/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^.*/accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'goflow/login.html'}),
    
    # static
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(_dir, 'media/img'), 'show_indexes': True}),
    url(r'^files/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # home redirection
    url(r'^.*/home/$',  RedirectView.as_view(url='/leave/')),
 
    # home page
    url(r'^leave/$', TemplateView.as_view(template_name='leave.html')),
    
    # starting application
    url(r'^leave/start/$', 'goflow.apptools.views.start_application', {'process_name':'leave',
                                                                           'form_class':StartRequestForm,
                                                                           'template':'start_leave.html'}),
    
    # applications
    url(r'^leave/checkstatus/(?P<id>.*)/$', 'goflow.apptools.views.edit_model', {'form_class':CheckRequestForm,
                                                                                     'template':'checkstatus.html'}),
    url(r'^leave/checkstatus_auto/$', 'leavedemo.leave.views.checkstatus_auto', {'notif_user':True}),
    url(r'^leave/refine/(?P<id>.*)/$', 'goflow.apptools.views.edit_model', {'form_class':RequesterForm,
                                                                                'template':'refine.html'}),
    url(r'^leave/approvalform/(?P<id>.*)/$', 'goflow.apptools.views.edit_model', {'form_class':CheckRequestForm,
                                                                                      'template':'approval.html'}),
    url(r'^leave/hrform/(?P<id>.*)/$', 'goflow.apptools.views.view_application', {'template':'hrform.html'}),
    url(r'^leave/hr_auto/$', 'leavedemo.leave.auto.update_hr'),
    url(r'^leave/finalinfo/(?P<id>.*)/$', 'goflow.apptools.views.view_application', {'template':'finalinfo.html'}),
    
     # administration
    url(r'^leave/admin/apptools/', include('goflow.apptools.urls_admin')),
    url(r'^leave/admin/workflow/', include('goflow.apptools.urls_admin')),
    url(r'^leave/admin/graphics2/', include('goflow.graphics2.urls_admin')),
    url(r'^leave/admin/(.*)', admin.site.urls),
    
    # Goflow pages
    url(r'^leave/', include('goflow.urls')),

    url(r'^leave/send_mail/$', 'goflow.workflow.notification.send_mail'),
    
)
