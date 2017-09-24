from django.conf.urls import url
from . import views


app_name='rfs'

urlpatterns=[
    url(r'^$',views.StartView,name='start'),
    url(r'^login/$',views.LoginView,name='login'),
    url(r'^dashboard/$',views.IndexView,name='index'),
    url(r'project/(?P<pk>[0-9]+)/details/$',views.ProjectDetail.as_view(),name='project'),
    url(r'project/create/$',views.ProjectCreate.as_view(),name='project-create'),
    #url(r'project/files/',views.FileView.as_view(),name='file-view'),
    #url(r'project/')
    #url(r'^signup/$',views.LoginView,name='signup'),
]