from django.conf.urls import url
from . import views


app_name='rfs'

urlpatterns=[
    url(r'^$', views.start_view, name='start'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),

    ########
    url(r'^home/$', views.index_view, name='index'),
    url(r'^home/upload_to/$',views.upload_file_to,name='upload_file_to'),

    url(r'dashboard/project/(?P<project_id>[0-9]+)/update/$', views.project_update_index, name='index-project-update'),

    ##PROJECT URLS##
    url(r'project/(?P<pk>[0-9]+)/$',views.ProjectDashboard.as_view(),name='project'),
    url(r'project/(?P<pk>[0-9]+)/details/$',views.ProjectDetails.as_view(),name='project-details'),

    url(r'project/create/$',views.ProjectCreate.as_view(),name='project-create'),
    url(r'project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project-delete'),
    ##FILE URLS##
    url(r'project/(?P<project_id>[0-9]+)/files/$', views.file_view, name='file'),
    url(r'project/(?P<project_id>[0-9]+)/files/(?P<file_id>[0-9]+)/update/$', views.file_update, name='file-delete'),
    url(r'project/(?P<project_id>[0-9]+)/files/archived/$',views.arc_file_view,name='arc-file'),
    url(r'project/(?P<project_id>[0-9]+)/files/archived/(?P<file_id>[0-9]+)/update/$',views.arc_file_update,name='arc-file-update'),
    #url(r'project/(?P<project_id>[0-9]+)/delete/(?P<file_id>[0-9]+)/$', views.file_delete_in_details, name='file-del'),
    ##DATA FEEDER URLS##
    url(r'project/(?P<project_id>[0-9]+)/datafeeder', views.excel_to_db, name='datafeed'),


    url(r'^forecast/$', views.forecast_form, name='forecast')
    #TEST#
    #url(r'^test/$',views.ActualView.as_view(),name='actual-view'),

    #url for forecast menu


]