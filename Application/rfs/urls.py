from django.conf.urls import url
from . import views


app_name='rfs'

urlpatterns=[
    url(r'^$', views.start_view, name='start'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^dashboard/$', views.index_view, name='index'),
    url(r'project/(?P<pk>[0-9]+)/$',views.ProjectDetail.as_view(),name='project'),
    url(r'project/create/$',views.ProjectCreate.as_view(),name='project-create'),
    url(r'project/(?P<pk>[0-9]+)/delete/$',views.ProjectDelete.as_view(),name='project-delete'),
    url(r'project/(?P<project_id>[0-9]+)/files/$', views.file_view, name='file'),
    url(r'project/(?P<project_id>[0-9]+)/files/(?P<file_id>[0-9]+)/delete/$', views.file_delete, name='file-delete'),
    url(r'project/(?P<project_id>[0-9]+)/delete/(?P<file_id>[0-9]+)/$', views.file_delete_in_details, name='file-del'),
    url(r'^test/$',views.read_excel,name='test'),
]