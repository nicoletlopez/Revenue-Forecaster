from django.conf.urls import url
from . import views

app_name='ajax'

urlpatterns=[
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', views.ChartData.as_view(), name='data'),
    url(r'^api/data/$', views.get_data, name='api-data')

]