from django.conf.urls import url
from . import views


app_name='rfs'

urlpatterns=[
    url(r'^$',views.StartView,name='start'),
    url(r'^login/$',views.LoginView,name='login'),
    url(r'^dashboard/$',views.IndexView,name='index'),
    url(r'project/(?P<pk>[0-9]+)/details/$',views.ProjectDetail.as_view(),name='project'),
    url(r'project/create/$',views.ProjectCreate.as_view(),name='project-create'),
    url(r'project/(?P<pk>[0-9]+)/delete/$',views.ProjectDelete.as_view(),name='project-delete'),
    url(r'project/(?P<project_id>[0-9]+)/files/add/$',views.FileAdd,name='file-add'),
    #url(r'project/(?P<project_id>[0-9]+)/files/(?P<file_id>[0-9]+)/delete/$',views.FileDelete,name='file-delete'),
    #url(r'project/')
    #url(r'^signup/$',views.LoginView,name='signup'),
]